from pathlib import Path

from app.config import SAMPLE_DOCS_DIR
from retrieval.chunking import chunk_text


def read_sample_documents(directory: Path = SAMPLE_DOCS_DIR) -> list[dict]:
    documents = []
    for path in sorted(directory.glob("*.md")):
        title = path.stem.replace("_", " ").title()
        documents.append({"source_id": path.stem, "document_title": title, "text": path.read_text(encoding="utf-8")})
    return documents


def ingest_documents(directory: Path = SAMPLE_DOCS_DIR) -> list[dict]:
    chunks: list[dict] = []
    for document in read_sample_documents(directory):
        chunks.extend(chunk_text(document["text"], document["source_id"], document["document_title"]))
    return chunks
