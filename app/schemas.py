from typing import Literal

from pydantic import BaseModel, Field


Confidence = Literal["low", "medium", "high"]


class DocumentIngestResponse(BaseModel):
    documents_ingested: int = Field(..., ge=0)
    chunks_indexed: int = Field(..., ge=0)


class ResearchRequest(BaseModel):
    question: str = Field(..., min_length=5, max_length=500)


class Citation(BaseModel):
    source_id: str = Field(..., min_length=1, max_length=120)
    document_title: str = Field(..., min_length=1, max_length=200)
    chunk_id: str = Field(..., min_length=1, max_length=120)
    quote: str = Field(..., min_length=1, max_length=500)


class AgentStep(BaseModel):
    agent: str
    output: dict


class ResearchResponse(BaseModel):
    run_id: int
    question: str
    direct_answer: str
    supporting_evidence: list[str]
    citations: list[Citation]
    uncertainty_notes: list[str]
    limitations: list[str]
    grounding_score: float = Field(..., ge=0, le=100)
    confidence: Confidence
    agent_trace: list[AgentStep]


class RunSummary(BaseModel):
    id: int
    question: str
    direct_answer: str
    grounding_score: float = Field(..., ge=0, le=100)
    confidence: Confidence
    created_at: str
