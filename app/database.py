import sqlite3
from pathlib import Path

from app.config import DATABASE_PATH


def get_connection(path: Path = DATABASE_PATH) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection


def init_db(path: Path = DATABASE_PATH) -> None:
    with get_connection(path) as connection:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS research_runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                direct_answer TEXT NOT NULL,
                grounding_score REAL NOT NULL,
                confidence TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS agent_steps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id INTEGER NOT NULL,
                agent TEXT NOT NULL,
                output_json TEXT NOT NULL,
                FOREIGN KEY(run_id) REFERENCES research_runs(id)
            );

            CREATE TABLE IF NOT EXISTS retrieved_chunks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id INTEGER NOT NULL,
                source_id TEXT NOT NULL,
                document_title TEXT NOT NULL,
                chunk_id TEXT NOT NULL,
                text TEXT NOT NULL,
                score REAL NOT NULL,
                FOREIGN KEY(run_id) REFERENCES research_runs(id)
            );

            CREATE TABLE IF NOT EXISTS final_answers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id INTEGER NOT NULL,
                answer_json TEXT NOT NULL,
                FOREIGN KEY(run_id) REFERENCES research_runs(id)
            );
            """
        )
