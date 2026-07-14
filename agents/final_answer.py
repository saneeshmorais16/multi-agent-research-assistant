def build_final_answer(question: str, summaries: list[dict], critic: dict, contradictions: dict) -> dict:
    if not summaries or critic["grounding_score"] < 20:
        return {
            "direct_answer": "The local sample knowledge base does not contain enough evidence to answer this question reliably.",
            "supporting_evidence": [],
            "citations": [],
            "uncertainty_notes": ["Evidence was insufficient or weakly related to the research question."],
            "limitations": ["This starter only answers from bundled sample documents."],
            "grounding_score": critic["grounding_score"],
            "confidence": "low",
        }

    top = summaries[:4]
    evidence = [item["summary"] for item in top]
    citations = [
        {
            "source_id": item["source_id"],
            "document_title": item["source_id"].replace("_", " ").title(),
            "chunk_id": item["chunk_id"],
            "quote": item["summary"][:220],
        }
        for item in top
    ]
    cited = " ".join(f"[{item['chunk_id']}]" for item in top[:3])
    answer = f"Based on the retrieved sample documents, {question.rstrip('?')} is best answered by combining the strongest cited evidence and noting limits. {cited}"
    return {
        "direct_answer": answer,
        "supporting_evidence": evidence,
        "citations": citations,
        "uncertainty_notes": critic["feedback"] + contradictions["contradictions_found"],
        "limitations": ["Uses local synthetic sample documents only.", "Rule-based workflow; optional LLM integration is not enabled by default."],
        "grounding_score": critic["grounding_score"],
        "confidence": critic["confidence"],
    }
