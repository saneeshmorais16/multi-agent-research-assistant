from agents.final_answer import build_final_answer


def test_final_answer_includes_citations():
    answer = build_final_answer(
        "How should RAG answer?",
        [{"source_id": "rag_systems", "chunk_id": "rag_systems#chunk-1", "summary": "Answers should cite retrieved chunks."}],
        {"grounding_score": 80, "confidence": "high", "feedback": []},
        {"contradictions_found": []},
    )
    assert answer["citations"][0]["chunk_id"] == "rag_systems#chunk-1"
    assert "[rag_systems#chunk-1]" in answer["direct_answer"]


def test_insufficient_evidence_behavior():
    answer = build_final_answer(
        "What private source says this?",
        [],
        {"grounding_score": 0, "confidence": "low", "feedback": ["No evidence"]},
        {"contradictions_found": []},
    )
    assert "does not contain enough evidence" in answer["direct_answer"]
