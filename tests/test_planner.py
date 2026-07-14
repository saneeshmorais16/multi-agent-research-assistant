from agents.planner import plan_research


def test_planner_creates_sub_questions():
    plan = plan_research("How can RAG systems reduce hallucination risk?")
    assert len(plan["sub_questions"]) >= 3
    assert "rag" in plan["focus_terms"]
