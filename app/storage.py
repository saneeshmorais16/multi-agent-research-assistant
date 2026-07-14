import json

from app.database import get_connection, init_db


def save_run(question: str, final_answer: dict, agent_trace: list[dict], retrieved_chunks: list[dict]) -> int:
    init_db()
    with get_connection() as connection:
        cursor = connection.execute(
            "INSERT INTO research_runs (question, direct_answer, grounding_score, confidence) VALUES (?, ?, ?, ?)",
            (question, final_answer["direct_answer"], final_answer["grounding_score"], final_answer["confidence"]),
        )
        run_id = int(cursor.lastrowid)
        for step in agent_trace:
            connection.execute(
                "INSERT INTO agent_steps (run_id, agent, output_json) VALUES (?, ?, ?)",
                (run_id, step["agent"], json.dumps(step["output"])),
            )
        for chunk in retrieved_chunks:
            connection.execute(
                """
                INSERT INTO retrieved_chunks (run_id, source_id, document_title, chunk_id, text, score)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (run_id, chunk["source_id"], chunk["document_title"], chunk["chunk_id"], chunk["text"], chunk["score"]),
            )
        connection.execute(
            "INSERT INTO final_answers (run_id, answer_json) VALUES (?, ?)",
            (run_id, json.dumps(final_answer)),
        )
    return run_id


def list_runs() -> list[dict]:
    init_db()
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT id, question, direct_answer, grounding_score, confidence, created_at FROM research_runs ORDER BY id DESC"
        ).fetchall()
    return [dict(row) for row in rows]


def get_run(run_id: int) -> dict | None:
    init_db()
    with get_connection() as connection:
        run = connection.execute("SELECT * FROM research_runs WHERE id = ?", (run_id,)).fetchone()
        if not run:
            return None
        steps = connection.execute("SELECT agent, output_json FROM agent_steps WHERE run_id = ? ORDER BY id", (run_id,)).fetchall()
        chunks = connection.execute("SELECT * FROM retrieved_chunks WHERE run_id = ? ORDER BY id", (run_id,)).fetchall()
        final = connection.execute("SELECT answer_json FROM final_answers WHERE run_id = ?", (run_id,)).fetchone()
    payload = dict(run)
    payload["agent_trace"] = [{"agent": row["agent"], "output": json.loads(row["output_json"])} for row in steps]
    payload["retrieved_chunks"] = [dict(row) for row in chunks]
    payload["final_answer"] = json.loads(final["answer_json"]) if final else {}
    return payload
