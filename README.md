# Multi-Agent Research Assistant

A portfolio-ready multi-agent research assistant that plans research questions, retrieves local evidence, summarises source chunks, checks contradictions, evaluates groundedness and produces a final cited answer.

## What This Project Does

The assistant accepts a research question, decomposes it into sub-questions, retrieves relevant chunks from safe sample documents and returns a structured answer with citations, uncertainty notes and an agent trace.

## Why It Matters

Agentic AI systems need more than a single prompt. Strong research workflows benefit from planning, retrieval, evidence summarisation, critic checks and explicit uncertainty handling.

## Problem Statement

LLM-style assistants can hallucinate when they answer without evidence. This project demonstrates a local, rule-based workflow that answers only from retrieved context and says when evidence is insufficient.

## Tech Stack

- Python
- FastAPI
- SQLite
- Deterministic local embedding vectors
- Pydantic structured outputs
- Optional LLM-compatible configuration placeholders
- pytest
- GitHub Actions
- HTML, CSS and JavaScript frontend

## Core Features

- Research question input
- Local sample document ingestion
- Chunking and embedding generation
- Vector-style retrieval
- Multi-agent workflow
- Grounded answer generation with citations
- Structured FastAPI response validation for confidence and grounding scores
- Agent trace and critic feedback
- SQLite storage for runs, steps, chunks and answers
- Simple frontend

## Multi-Agent Architecture

```text
User Question
  -> Planner Agent
  -> Retriever Agent
  -> Summariser Agent
  -> Contradiction Checker Agent
  -> Critic / Evaluator Agent
  -> Final Answer Agent
```

## RAG / Retrieval Explanation

Sample Markdown documents are chunked into short passages. Each chunk receives a deterministic local embedding vector built from hashed tokens. Retrieval compares the question or sub-question vector with chunk vectors and returns the highest-scoring chunks with source and chunk identifiers.

## Example Research Question

```text
How should teams reduce hallucination risk in RAG systems?
```

## Example Agent Trace

```json
{
  "planner": ["What evidence explains the question?", "What risks or limitations relate to the question?"],
  "retriever": ["rag_systems#chunk-1", "ai_governance#chunk-1"],
  "critic": {"grounding_score": 78.5, "confidence": "high"}
}
```

## Example Final Answer With Citations

```text
Teams should reduce hallucination risk by retrieving inspectable source chunks, requiring citations and refusing to answer when retrieved context is weak. [rag_systems#chunk-1] [ai_governance#chunk-1]
```

## Setup Steps

```bash
pip install -r requirements.txt
```

## Run The API

```bash
python run.py
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/` for the simple frontend.

## Run Tests

```bash
pytest
```

## Responsible AI / Limitations

This starter uses safe sample documents and rule-based agents. It does not use private documents, user conversations or external LLM APIs by default. It should not be described as production deployed, used by real users or enterprise-ready. Retrieval quality is intentionally lightweight and should be evaluated before serious use.

## Future Improvements

- Add optional OpenAI or Anthropic-compatible LLM review with explicit user keys.
- Add a production vector database option such as ChromaDB.
- Add richer citation span extraction and reranking.
- Add document upload with strict privacy controls.
- Add evaluation datasets for retrieval and answer quality.

## No-Secrets Note

Do not commit `.env` files, API keys, tokens, credentials, private documents, private prompts, user conversations, logs, generated PDFs, application packets, databases or generated outputs.
