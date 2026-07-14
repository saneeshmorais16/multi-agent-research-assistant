import re


def summarise_evidence(question: str, chunks: list[dict]) -> dict:
    summaries = []
    for chunk in chunks:
        sentences = re.split(r"(?<=[.!?])\s+", chunk["text"])
        selected = sentences[0][:260] if sentences else chunk["text"][:260]
        summaries.append(
            {
                "source_id": chunk["source_id"],
                "chunk_id": chunk["chunk_id"],
                "summary": selected,
                "score": chunk["score"],
            }
        )
    return {"question": question, "evidence_summaries": summaries}
