"""Held-out governance scenarios for F166."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"role_context_gap": True}, False),
    (base() | {"candidate_evidence_gap": True}, False),
    (base() | {"story_truthfulness_gap": True}, False),
    (base() | {"question_strategy_gap": True}, False),
    (base() | {"mock_interview_gap": True}, False),
    (base() | {"feedback_fairness_risk": True}, False),
    (base() | {"privacy_confidentiality_risk": True}, False),
    (base() | {"provenance_approval_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_interview_coaching_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F166 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
