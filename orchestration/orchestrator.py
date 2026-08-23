from AGENTS import feedback_agent, mock_agent, question_agent, role_agent, story_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "role": role_agent.run(case),
        "story": story_agent.run(case),
        "questions": question_agent.run(case),
        "mock": mock_agent.run(case),
        "feedback": feedback_agent.run(case),
    }
    governance = authorize("release_interview_coaching_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
