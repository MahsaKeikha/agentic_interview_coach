# F166 | Agentic Interview Coach | L3 Gold Standard | v1.0

A governed five-agent reference architecture for interview preparation across role analysis, evidence-grounded stories, question strategy, mock interviews, feedback, fairness, privacy, confidentiality, and candidate-controlled approval.

F166 is a coaching and rehearsal system. It is not the candidate, recruiter, hiring manager, employer, reference, background-check service, immigration adviser, employment lawyer, or autonomous application system. It cannot fabricate qualifications, impersonate the candidate, submit applications, accept offers, contact employers as the candidate, disclose protected information, or deceive interview assessments.

## Interview-preparation lifecycle

```text
Role, Company, and Interview Context
        -> Candidate Evidence and Experience Map
        -> Truthful Story Development
        -> Question and Answer Strategy
        -> Mock Interview and Follow-up Practice
        -> Evidence-Based Feedback
        -> Candidate Review and Approval
        -> Candidate-Controlled Interview
```

The workflow fails closed when required reviews are missing or when material role-context, candidate-evidence, story-truthfulness, question-strategy, rehearsal, feedback-fairness, privacy, confidentiality, provenance, or approval issues remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Role Agent | Structures role requirements, company context, level, competencies, interview format, stakeholders, and evaluation criteria | What is this interview actually assessing? |
| Story Agent | Maps verified candidate experience into truthful behavioral, leadership, technical, and achievement stories | Which real experiences best demonstrate the relevant competencies? |
| Question Agent | Develops likely questions, answer frameworks, technical scope, follow-ups, and candidate questions | What should the candidate be ready to explain, demonstrate, and ask? |
| Mock Agent | Simulates interview sequences, follow-ups, cases, technical exercises, presentations, and timing | Can the candidate perform under realistic interview conditions? |
| Feedback Agent | Synthesizes observable strengths, gaps, answer quality, evidence use, clarity, and improvement priorities | What changes would most improve the candidate's next attempt? |

## Repository structure

```text
AGENTS/
├── role_agent.py
├── story_agent.py
├── question_agent.py
├── mock_agent.py
└── feedback_agent.py

SKILLS/
├── role_analysis.py
├── star_storytelling.py
├── question_reasoning.py
├── mock_interviewing.py
└── feedback_synthesis.py

TOOLS/
├── evidence_ledger.py
├── story_bank.py
├── question_bank.py
├── scorecard.py
└── approval_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Role analysis

The executable policy requires `role_context_reviewed`. `role_context_gap` blocks release when material role, company, interview format, competency, level, stakeholder, or evaluation-context issues remain unresolved.

Role analysis can include responsibilities, required and preferred qualifications, seniority, domain, leadership scope, technical depth, customer exposure, communication demands, location, travel, and stated evaluation process.

## Job-description interpretation

A job description is evidence about the role, not a complete representation of the employer's internal scorecard. F166 should distinguish explicit requirements from inferred priorities.

## Company context

Preparation can include public company information, products, customers, mission, business model, competitors, recent developments, and role-relevant challenges when reliable evidence is available.

## Interview format

The system can prepare for recruiter screens, hiring-manager interviews, behavioral rounds, technical interviews, coding interviews, system design, case interviews, portfolio reviews, presentations, panels, executive interviews, and final rounds.

## Candidate evidence

The executable policy requires `candidate_evidence_reviewed`. `candidate_evidence_gap` blocks release when material employment, education, skill, project, achievement, metric, credential, or experience claims lack candidate evidence.

Candidate evidence can include resumes, portfolios, publications, project records, performance evidence, job history, education, credentials, and candidate-confirmed experiences.

## Truthfulness boundary

`fabricate_or_exaggerate_candidate_claim` is protected. Interview coaching must not invent employers, titles, dates, degrees, certifications, projects, customers, patents, publications, metrics, leadership responsibilities, technical skills, awards, or outcomes.

## Ownership

The candidate should distinguish work they personally performed from team outcomes, organizational results, or work led by others.

## Metrics

Numbers should be used when supported. Approximate metrics should be labeled appropriately rather than converted into false precision.

## Confidential work

A candidate can demonstrate competence without revealing trade secrets, proprietary architecture, customer identities, unreleased products, source code, security details, privileged information, or NDA-protected material.

## Story architecture

The executable policy requires `story_truthfulness_reviewed`. `story_truthfulness_gap` blocks release when a material interview story, attribution, action, result, ownership, chronology, or lesson is fabricated, exaggerated, or misleading.

## STAR and alternatives

Situation, Task, Action, Result can help structure behavioral answers, but F166 should not force every answer into a rigid formula. Context, decision, action, tradeoff, result, learning, and reflection can also be useful.

## Situation

Context should be sufficient to understand the challenge without consuming most of the answer.

## Task

The candidate's actual responsibility should be distinguished from the team's broader mission.

## Action

Actions should explain what the candidate personally decided, built, changed, analyzed, communicated, or led.

## Result

Results should preserve uncertainty and attribution. Team or company outcomes should not be claimed as solely caused by the candidate without evidence.

## Learning

Reflection can show judgment, growth, and adaptation. It should not be manufactured merely to create a perfect narrative arc.

## Failure stories

A useful failure answer can show accountability, analysis, correction, and learning without inventing a harmless fake failure.

## Conflict stories

Conflict answers should avoid disclosing private personnel information or portraying colleagues unfairly when details are unnecessary.

## Leadership stories

Leadership can include formal management, technical leadership, influence, mentoring, decision making, cross-functional coordination, incident response, ownership, and organizational change.

## Ambiguity stories

Examples can demonstrate how the candidate gathered information, formed hypotheses, made decisions, communicated uncertainty, and adapted.

## Technical stories

Technical answers should preserve architecture, constraints, alternatives, tradeoffs, validation, failure modes, and the candidate's actual contribution.

## Question strategy

The executable policy requires `question_strategy_reviewed`. `question_strategy_gap` blocks release when material question interpretation, answer strategy, technical scope, behavioral competency, or candidate-question issues remain unresolved.

## Behavioral questions

Behavioral preparation should map competencies to multiple real examples so the candidate can adapt rather than memorize one answer per question.

## Technical questions

Preparation should reflect the actual role. F166 should not imply mastery of tools or concepts the candidate cannot explain independently.

## Coding interviews

The coach can practice problem clarification, examples, algorithm selection, complexity, implementation, testing, edge cases, and communication.

It should not facilitate prohibited real-time cheating in an active assessment.

## System design

Preparation can cover requirements, scale, APIs, data models, architecture, reliability, security, observability, tradeoffs, bottlenecks, and evolution.

## Case interviews

Case practice can develop structure, assumptions, calculations, synthesis, and communication while preserving uncertainty and avoiding memorized deceptive scripts.

## Product interviews

Preparation can include user needs, prioritization, metrics, product sense, execution, experimentation, tradeoffs, and strategy.

## Research interviews

Research candidates can prepare to discuss hypotheses, methods, findings, limitations, reproducibility, failures, open questions, and future work.

## Executive interviews

Executive preparation can emphasize strategy, leadership, organizational design, capital allocation, governance, stakeholder management, risk, culture, and decision quality.

## Candidate questions

The candidate should prepare questions that genuinely help evaluate role scope, manager expectations, team health, decision authority, resources, strategy, culture, growth, and constraints.

## Compensation questions

F166 can help prepare communication about compensation expectations and tradeoffs, but binding negotiation, legal, tax, immigration, and offer decisions remain with the candidate and qualified professionals where appropriate.

## Mock interviews

The executable policy requires `mock_interview_reviewed`. `mock_interview_gap` blocks release when material rehearsal, timing, follow-up, technical exercise, case, presentation, or interview-readiness issues remain unresolved.

## Realistic simulation

Mocks should include realistic sequencing, ambiguity, interruptions, follow-up questions, time constraints, and interviewer challenge appropriate to the role.

## Progressive difficulty

Practice can begin with familiar questions and progress toward ambiguous, adversarial, technical, cross-functional, or executive-level follow-ups.

## Timing

Answers should be long enough to establish evidence but short enough to preserve interaction. Appropriate length depends on question and interview format.

## Follow-ups

Strong preparation includes second-order questions such as why, what alternatives were considered, what failed, what the candidate would change, and how results were measured.

## Presentation interviews

Preparation can include structure, evidence, slides, timing, Q&A, assumptions, accessibility, and technology contingencies.

## Remote interviews

Remote preparation can include audio, camera, lighting, connectivity, screen sharing, coding environment, notifications, backup contact methods, and privacy.

## In-person interviews

Preparation can include travel margin, venue logistics, materials, accessibility, schedule, breaks, and practical contingencies.

## Feedback architecture

The executable policy requires `feedback_fairness_reviewed`. `feedback_fairness_risk` blocks release when material feedback relies on unsupported personality inference, protected traits, accent bias, disability bias, cultural bias, or irrelevant appearance judgments.

## Observable feedback

Feedback should focus on answer evidence, relevance, structure, clarity, concision, technical correctness, reasoning, ownership, listening, and question handling.

## Personality inference

A short answer does not prove low confidence. Limited eye contact does not prove dishonesty. Accent does not indicate competence. F166 should not turn superficial signals into psychological conclusions.

## Accent and language

Coaching can improve intelligibility and clarity without pressuring candidates to erase cultural or linguistic identity.

## Disability and neurodiversity

Interview feedback should not penalize disability-related communication differences or neurodivergent traits unrelated to role requirements.

## Appearance

The coach can discuss stated dress expectations when relevant but should not rank attractiveness, body type, age presentation, race, gender expression, or other protected or irrelevant traits.

## Cultural variation

Communication norms differ across cultures. Directness, eye contact, self-promotion, pauses, hierarchy, and storytelling should not be judged through one cultural standard without context.

## Scorecards

Scorecards can support structured practice but should not be presented as validated predictors of hiring outcomes unless evidence supports that claim.

## Hiring prediction

F166 should not promise that a candidate will receive an offer or assign false probabilities based on limited interview practice.

## Privacy and confidentiality

The executable policy requires `privacy_confidentiality_reviewed`. `privacy_confidentiality_risk` blocks release when material privacy, NDA, trade-secret, employer-confidential, personal-data, reference, or third-party-consent issues remain unresolved.

## Prior-employer confidentiality

Candidates should avoid exposing proprietary roadmaps, customer data, source code, internal incidents, pricing, security vulnerabilities, unpublished research, personnel matters, or other protected information.

## Current-employer sensitivity

Job searching can itself be sensitive. F166 should not contact employers, references, coworkers, or recruiters without explicit authorization.

## Reference boundary

`contact_employer_recruiter_or_reference_as_candidate` is protected. The coach can draft communication, not send it as the candidate.

## Personal data

Interview materials can contain addresses, phone numbers, work authorization, compensation, family information, disability information, and other sensitive data. Collection should be minimized.

## Protected characteristics

The coach should not recommend disclosing protected characteristics merely to influence a hiring decision.

## Illegal or inappropriate questions

The system can help a candidate recognize potentially inappropriate questions and prepare boundary-preserving responses, while jurisdiction-specific legal advice should come from qualified sources.

## Assessment integrity

`bypass_interview_assessment_or_deceive_evaluator` is protected. F166 supports preparation before an interview, not covert assistance that violates active assessment rules.

## Real-time assistance

If an employer permits tools during an assessment, use should follow those rules. The system should not help conceal prohibited assistance.

## Take-home assignments

Candidates should follow stated collaboration and AI-use policies. F166 can coach reasoning and review work but should not falsely represent generated work as independently completed when disclosure is required.

## Candidate approval

The executable policy requires `candidate_approval_reviewed`. The candidate retains final authority over stories, answers, questions, disclosure, negotiation, applications, and employment decisions.

## Protected actions

```text
fabricate_or_exaggerate_candidate_claim
impersonate_candidate_in_interview
submit_application_or_accept_offer
contact_employer_recruiter_or_reference_as_candidate
disclose_confidential_or_sensitive_information
bypass_interview_assessment_or_deceive_evaluator
```

These remain outside autonomous authority even after all required reviews pass.

## Application and offer boundary

`submit_application_or_accept_offer` is protected. Interview preparation does not authorize job application submission, offer acceptance, resignation, or other consequential employment actions.

## Impersonation boundary

`impersonate_candidate_in_interview` is protected. F166 cannot participate in an interview while pretending to be the candidate.

## Provenance

`provenance_approval_gap` blocks release when material evidence, story, answer, feedback, revision, source, or candidate-approval provenance is incomplete.

F166 must never fabricate candidate experience, role requirements, company facts, interviewer identities, interview feedback, recruiter statements, compensation, hiring decisions, references, credentials, approvals, or completed actions.

## Required reviews

The executable policy requires all eight conditions:

```text
role_context_reviewed
candidate_evidence_reviewed
story_truthfulness_reviewed
question_strategy_reviewed
mock_interview_reviewed
feedback_fairness_reviewed
privacy_confidentiality_reviewed
candidate_approval_reviewed
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- role, company, interview format, competency, level, stakeholder, or evaluation context remains materially unresolved
- employment, education, skills, projects, achievements, metrics, credentials, or experience claims lack evidence
- interview stories, attribution, actions, results, ownership, chronology, or lessons are fabricated, exaggerated, or misleading
- question interpretation, answer strategy, technical scope, behavioral competencies, or candidate questions remain materially unresolved
- rehearsal, timing, follow-ups, technical exercises, cases, presentations, or interview readiness remain materially unresolved
- feedback relies on unsupported personality inference, protected traits, accent bias, disability bias, cultural bias, or irrelevant appearance judgments
- privacy, NDA, trade-secret, employer-confidential, personal-data, reference, or third-party-consent issues remain unresolved
- evidence, stories, answers, feedback, revisions, sources, or candidate approvals lack provenance
- any required review is missing
- candidate approval review is missing

## Explicit failure states

```text
ROLE AND INTERVIEW CONTEXT REVIEW REQUIRED
CANDIDATE EVIDENCE REVIEW REQUIRED
STORY TRUTHFULNESS REVIEW REQUIRED
QUESTION STRATEGY REVIEW REQUIRED
MOCK INTERVIEW REVIEW REQUIRED
FEEDBACK AND FAIRNESS REVIEW REQUIRED
PRIVACY AND CONFIDENTIALITY REVIEW REQUIRED
CANDIDATE APPROVAL REVIEW REQUIRED
ROLE OR CONTEXT GAP
CANDIDATE EVIDENCE GAP
STORY TRUTHFULNESS GAP
QUESTION STRATEGY GAP
MOCK INTERVIEW READINESS GAP
FEEDBACK OR FAIRNESS RISK
PRIVACY OR CONFIDENTIALITY RISK
PROVENANCE OR APPROVAL GAP
CANDIDATE CLAIM FABRICATION PROHIBITED
CANDIDATE IMPERSONATION PROHIBITED
AUTONOMOUS APPLICATION OR OFFER ACTION PROHIBITED
UNAUTHORIZED EMPLOYER OR REFERENCE CONTACT PROHIBITED
UNAUTHORIZED SENSITIVE DISCLOSURE PROHIBITED
ASSESSMENT DECEPTION PROHIBITED
```

## End-to-end reference workflow

1. Capture role, company, level, interview stages, format, competencies, logistics, and candidate goals.
2. Build an evidence ledger for employment, education, projects, skills, leadership, achievements, metrics, and credentials.
3. Map real candidate experiences to likely behavioral, technical, leadership, collaboration, failure, ambiguity, and conflict competencies.
4. Structure truthful stories with clear ownership, actions, tradeoffs, results, and lessons.
5. Build question banks for role-specific behavioral, technical, case, system-design, product, research, or executive topics.
6. Prepare candidate questions that help evaluate the employer and role rather than treating the interview as one-way evaluation.
7. Run mock interviews with realistic timing, follow-ups, ambiguity, technical exercises, cases, presentations, and Q&A.
8. Give evidence-based feedback focused on relevance, clarity, reasoning, ownership, technical quality, and communication rather than protected traits or unsupported personality inference.
9. Review NDA, confidentiality, trade-secret, privacy, reference, assessment-integrity, and third-party-consent boundaries.
10. Preserve provenance for evidence, stories, answers, feedback, revisions, and approvals.
11. Apply fail-closed governance and present the preparation package for explicit candidate review.
12. Keep application submission, offer acceptance, employer contact, candidate impersonation, fabricated claims, and assessment deception outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test role relevance, evidence fidelity, story truthfulness, ownership, question quality, technical scope, mock realism, feedback usefulness, fairness, confidentiality, assessment integrity, provenance, approval, and protected-action behavior.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved coaching-package release, role-context gaps, candidate-evidence gaps, story-truthfulness gaps, question-strategy gaps, mock-interview gaps, feedback-fairness risks, privacy-confidentiality risks, and provenance-approval gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed governance, held-out scenarios, and execution of the governed five-agent interview-coaching workflow.

## Memory and state

The `memory/` layer can preserve candidate-approved role context, evidence, story versions, question banks, mock results, feedback, unresolved gaps, and approval state.

Stale resumes, old target roles, outdated company information, or superseded candidate corrections should not silently override current evidence.

## Observability

The `observability/` layer supports traceability across evidence intake, story revisions, question preparation, mock sessions, feedback, protected-action attempts, and candidate approvals.

Useful telemetry includes unsupported claims, repeated weak competencies, overlong answers, unresolved confidentiality issues, stale company evidence, assessment-integrity flags, and packages awaiting candidate approval.

## Reproducibility

A reproducible preparation package should preserve role version, job description, company evidence date, candidate evidence set, story versions, question bank, mock conditions, feedback source, revisions, unresolved issues, and approval state.

## Extension points

Organization-specific implementations can add governed integrations for resumes, portfolios, job descriptions, calendars, video rehearsal, coding sandboxes, whiteboards, transcription, scorecards, and learning systems.

Any integration capable of submitting applications, sending messages, contacting references, entering interviews, sharing candidate data, or accepting employment terms should remain behind explicit candidate authorization and clear previews.

## Example applications

Potential governed uses include behavioral interviews, software engineering interviews, system design, product management, data science, research, executive leadership, consulting cases, academic interviews, portfolio reviews, panel interviews, technical presentations, and recruiter screens.

F166 is not an autonomous candidate, recruiter, hiring decision maker, employment lawyer, immigration adviser, background-check system, or substitute for candidate judgment.

## Design principles

1. Ground every candidate claim and interview story in real evidence.
2. Preserve personal ownership, chronology, attribution, uncertainty, and confidentiality.
3. Optimize for authentic competence rather than memorized deception.
4. Practice realistic follow-ups, ambiguity, technical depth, and candidate questions.
5. Keep feedback focused on role-relevant observable behavior rather than protected traits or unsupported personality judgments.
6. Respect employer assessment rules and prohibit concealed real-time cheating.
7. Never fabricate qualifications, stories, metrics, company facts, interviewer feedback, or approvals.
8. Fail closed when role context, evidence, truthfulness, strategy, rehearsal, fairness, privacy, provenance, or candidate approval is incomplete.
9. Keep applications, offers, external contact, candidate representation, and consequential employment decisions under explicit human control.

## Scope statement

F166 demonstrates a governed multi-agent architecture for interview coaching. It combines specialized role, story, question, mock, and feedback agents with deterministic evidence, story, question, scorecard, and approval tools, observability, held-out evaluation, and fail-closed governance while preserving strict candidate authority over claims, disclosure, applications, offers, external representation, and actual interview performance.

Author: Mahsa Keikha
