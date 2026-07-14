from pydantic import BaseModel, Field


class DocumentIngestResponse(BaseModel):
    documents_ingested: int
    chunks_indexed: int


class ResearchRequest(BaseModel):
    question: str = Field(..., min_length=5, max_length=500)


class Citation(BaseModel):
    source_id: str
    document_title: str
    chunk_id: str
    quote: str


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
    grounding_score: float
    confidence: str
    agent_trace: list[AgentStep]


class RunSummary(BaseModel):
    id: int
    question: str
    direct_answer: str
    grounding_score: float
    created_at: str
