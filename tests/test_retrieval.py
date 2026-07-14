from retrieval.vector_store import InMemoryVectorStore


def test_retrieval_returns_relevant_chunk_first():
    store = InMemoryVectorStore()
    store.add_chunks(
        [
            {"source_id": "a", "document_title": "A", "chunk_id": "a#1", "text": "RAG systems use retrieval and citations."},
            {"source_id": "b", "document_title": "B", "chunk_id": "b#1", "text": "Cooking notes about bread."},
        ]
    )
    result = store.search("retrieval citations", top_k=1)
    assert result[0]["chunk_id"] == "a#1"
