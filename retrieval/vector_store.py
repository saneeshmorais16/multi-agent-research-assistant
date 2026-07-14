from retrieval.embeddings import cosine_similarity, embed_text


class InMemoryVectorStore:
    def __init__(self) -> None:
        self._records: list[dict] = []

    def reset(self) -> None:
        self._records = []

    def add_chunks(self, chunks: list[dict]) -> None:
        self._records = [{**chunk, "embedding": embed_text(chunk["text"])} for chunk in chunks]

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        query_embedding = embed_text(query)
        results = []
        for record in self._records:
            score = cosine_similarity(query_embedding, record["embedding"])
            results.append({key: value for key, value in record.items() if key != "embedding"} | {"score": round(score, 4)})
        return sorted(results, key=lambda item: item["score"], reverse=True)[:top_k]

    def sources(self) -> list[dict]:
        seen = {}
        for record in self._records:
            seen[record["source_id"]] = {"source_id": record["source_id"], "document_title": record["document_title"]}
        return sorted(seen.values(), key=lambda item: item["source_id"])


VECTOR_STORE = InMemoryVectorStore()
