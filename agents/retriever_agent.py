from retrieval.retrieval import retrieve_context


def retrieve_for_plan(plan: dict, top_k_per_question: int = 3) -> dict:
    seen = {}
    for sub_question in plan["sub_questions"]:
        for chunk in retrieve_context(sub_question, top_k=top_k_per_question):
            if chunk["chunk_id"] not in seen:
                seen[chunk["chunk_id"]] = chunk
    chunks = sorted(seen.values(), key=lambda item: item["score"], reverse=True)
    return {"retrieved_chunks": chunks[:8], "chunk_count": len(chunks[:8])}
