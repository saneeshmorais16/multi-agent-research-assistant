# Project Status

## Current Build Status

Working starter version for local portfolio review. The system runs without an LLM API key using rule-based agents and local deterministic retrieval over safe sample documents.

## Completed Features

- Planner agent
- Retriever agent
- Summariser agent
- Critic / evaluator agent
- Contradiction checker agent
- Final answer agent
- Local sample document ingestion
- Chunking and deterministic embedding generation
- Vector-style retrieval
- Citation-based answer output
- Insufficient-evidence behavior
- Agent trace
- SQLite storage for runs, steps, chunks and answers
- FastAPI endpoints
- Simple HTML/CSS/JavaScript frontend
- pytest test suite
- GitHub Actions workflow

## Remaining Improvements

- Add optional real embedding model integration.
- Add optional LLM provider wrapper with explicit user configuration.
- Add ChromaDB persistence as an alternate vector store.
- Add document upload with privacy controls.
- Add richer benchmark/evaluation reports.
- Add screenshots after local frontend review.

## Testing Status

Tests cover question planning, chunking, retrieval, citation extraction, insufficient-evidence behavior, critic scoring, health endpoint and research endpoint.

Run:

```bash
pytest
```

## What Must Be Checked Before Making Public

- No `.env` files or credentials are present.
- No private documents, prompts or research data are present.
- No real user conversations or personal data are present.
- No database files, logs, PDFs or generated outputs are committed.
- README does not claim production use, real users, clients or enterprise deployment.

## Files That Must Never Be Committed

- `.env` or `.env.*`
- API keys, tokens, credentials or passwords
- private documents
- private research
- private prompts
- user conversations
- personal data
- database files
- logs
- generated CV PDFs
- application packets
- generated outputs
- uploaded files
- local data
