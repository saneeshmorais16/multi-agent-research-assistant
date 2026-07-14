import re


def chunk_text(text: str, source_id: str, document_title: str, chunk_size: int = 90, overlap: int = 20) -> list[dict]:
    words = re.findall(r"\b[\w/-]+\b", text)
    chunks = []
    start = 0
    index = 1
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk_words = words[start:end]
        if chunk_words:
            chunks.append(
                {
                    "source_id": source_id,
                    "document_title": document_title,
                    "chunk_id": f"{source_id}#chunk-{index}",
                    "text": " ".join(chunk_words),
                }
            )
        if end == len(words):
            break
        start = max(end - overlap, start + 1)
        index += 1
    return chunks
