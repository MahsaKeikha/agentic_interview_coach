"""Fail-closed governance for F166 Agentic Interview Coach."""

PROTECTED_ACTIONS = {
    "fabricate_or_exaggerate_candidate_claim",
    "impersonate_candidate_in_interview",
    "submit_application_or_accept_offer",
    "contact_employer_recruiter_or_reference_as_candidate",
    "disclose_confidential_or_sensitive_information",
    "bypass_interview_assessment_or_deceive_evaluator",
}

REQUIRED_REVIEWS = (
    "role_context_reviewed",
    "candidate_evidence_reviewed",
    "story_truthfulness_reviewed",
    "question_strategy_reviewed",
    "mock_interview_reviewed",
    "feedback_fairness_reviewed",
    "privacy_confidentiality_reviewed",
    "candidate_approval_reviewed",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "fabrication, impersonation, consequential employment action, unauthorized contact, sensitive disclosure, or assessment deception is outside coach authority"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required interview-coaching review", "missing": missing}
    checks = {
        "role_context_gap": "material role, company, interview format, competency, level, stakeholder, or evaluation-context issue remains unresolved",
        "candidate_evidence_gap": "material employment, education, skill, project, achievement, metric, credential, or experience claim lacks candidate evidence",
        "story_truthfulness_gap": "material interview story, attribution, action, result, ownership, chronology, or lesson is fabricated, exaggerated, or misleading",
        "question_strategy_gap": "material question interpretation, answer strategy, technical scope, behavioral competency, or candidate-question issue remains unresolved",
        "mock_interview_gap": "material rehearsal, timing, follow-up, technical exercise, case, presentation, or interview-readiness issue remains unresolved",
        "feedback_fairness_risk": "material feedback relies on unsupported personality inference, protected traits, accent bias, disability bias, cultural bias, or irrelevant appearance judgments",
        "privacy_confidentiality_risk": "material privacy, NDA, trade-secret, employer-confidential, personal-data, reference, or third-party-consent issue remains unresolved",
        "provenance_approval_gap": "material evidence, story, answer, feedback, revision, source, or candidate-approval provenance is incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "interview-coaching governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "interview-coaching package approved for candidate-controlled use"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
