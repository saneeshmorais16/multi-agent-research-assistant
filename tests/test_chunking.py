from retrieval.chunking import chunk_text


def test_chunking_creates_cited_chunks():
    chunks = chunk_text("one two three four five six seven", "demo", "Demo", chunk_size=3, overlap=1)
    assert len(chunks) == 3
    assert chunks[0]["chunk_id"] == "demo#chunk-1"
