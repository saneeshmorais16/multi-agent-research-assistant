from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_research_endpoint():
    client.post("/documents/ingest")
    response = client.post("/research", json={"question": "How should teams reduce hallucination risk in RAG systems?"})
    assert response.status_code == 200
    payload = response.json()
    assert payload["agent_trace"]
    assert "direct_answer" in payload
    assert payload["citations"]
    assert 0 <= payload["grounding_score"] <= 100
    assert payload["confidence"] in {"low", "medium", "high"}


def test_research_endpoint_rejects_short_questions():
    response = client.post("/research", json={"question": "RAG?"})
    assert response.status_code == 422
