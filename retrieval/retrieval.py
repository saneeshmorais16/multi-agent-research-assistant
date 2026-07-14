from retrieval.ingestion import ingest_documents
from retrieval.vector_store import VECTOR_STORE


def ensure_indexed() -> int:
    if not VECTOR_STORE.sources():
        chunks = ingest_documents()
        VECTOR_STORE.add_chunks(chunks)
        return len(chunks)
    return 0


def rebuild_index() -> int:
    chunks = ingest_documents()
    VECTOR_STORE.reset()
    VECTOR_STORE.add_chunks(chunks)
    return len(chunks)


def retrieve_context(query: str, top_k: int = 5) -> list[dict]:
    ensure_indexed()
    return VECTOR_STORE.search(query, top_k=top_k)


def list_sources() -> list[dict]:
    ensure_indexed()
    return VECTOR_STORE.sources()
