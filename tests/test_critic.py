from agents.critic import evaluate_grounding


def test_critic_scores_grounded_answer():
    result = evaluate_grounding(
        "How do RAG systems use citations?",
        [{"summary": "RAG systems return retrieved chunks with citations and source identifiers."}],
    )
    assert result["grounding_score"] > 40
    assert result["confidence"] in {"medium", "high"}
