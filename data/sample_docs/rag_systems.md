# RAG Systems Notes

Retrieval augmented generation combines a question, a search step, retrieved chunks, and an answer generator. The retrieval step should return source identifiers, chunk identifiers, and short passages that can be inspected.

Good RAG systems use chunking, embeddings, keyword overlap, reranking, and citation display. If retrieved context is weak, the answer should say the evidence is insufficient rather than inventing details.

Contradiction checks are useful when sources disagree. A system can compare retrieved chunks, flag caution language, and ask for additional evidence before presenting a confident conclusion.
