from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from agents.contradiction_checker import check_contradictions
from agents.critic import evaluate_grounding
from agents.final_answer import build_final_answer
from agents.planner import plan_research
from agents.retriever_agent import retrieve_for_plan
from agents.summariser import summarise_evidence
from app.config import BASE_DIR
from app.database import init_db
from app.schemas import DocumentIngestResponse, ResearchRequest, ResearchResponse
from app.storage import get_run, list_runs, save_run
from retrieval.ingestion import read_sample_documents
from retrieval.retrieval import list_sources, rebuild_index

@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_db()
    rebuild_index()
    yield


app = FastAPI(title="Multi-Agent Research Assistant", version="0.1.0", lifespan=lifespan)
app.mount("/static", StaticFiles(directory=BASE_DIR / "app" / "static"), name="static")


@app.get("/")
def index():
    return FileResponse(BASE_DIR / "app" / "static" / "index.html")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "mode": "rule-based"}


@app.post("/documents/ingest", response_model=DocumentIngestResponse)
def ingest_documents_endpoint() -> DocumentIngestResponse:
    chunks = rebuild_index()
    docs = read_sample_documents()
    return DocumentIngestResponse(documents_ingested=len(docs), chunks_indexed=chunks)


@app.post("/research", response_model=ResearchResponse)
def research(request: ResearchRequest) -> dict:
    plan = plan_research(request.question)
    retrieved = retrieve_for_plan(plan)
    summary = summarise_evidence(request.question, retrieved["retrieved_chunks"])
    contradictions = check_contradictions(retrieved["retrieved_chunks"])
    draft_text = " ".join(item["summary"] for item in summary["evidence_summaries"])
    critic = evaluate_grounding(request.question, summary["evidence_summaries"], draft_text)
    final_answer = build_final_answer(request.question, summary["evidence_summaries"], critic, contradictions)
    trace = [
        # Keep the trace ordered so a reviewer can see the full research workflow.
        {"agent": "planner", "output": plan},
        {"agent": "retriever", "output": retrieved},
        {"agent": "summariser", "output": summary},
        {"agent": "contradiction_checker", "output": contradictions},
        {"agent": "critic", "output": critic},
        {"agent": "final_answer", "output": final_answer},
    ]
    run_id = save_run(request.question, final_answer, trace, retrieved["retrieved_chunks"])
    return {"run_id": run_id, "question": request.question, **final_answer, "agent_trace": trace}


@app.get("/runs")
def runs() -> list[dict]:
    return list_runs()


@app.get("/runs/{run_id}")
def run_detail(run_id: int) -> dict:
    run = get_run(run_id)
    if not run:
        raise HTTPException(status_code=404, detail="Run not found")
    return run


@app.get("/sources")
def sources() -> list[dict]:
    return list_sources()
