import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
SAMPLE_DOCS_DIR = DATA_DIR / "sample_docs"
OUTPUT_DIR = DATA_DIR / "outputs"
DATABASE_PATH = BASE_DIR / "multi_agent_research.db"
VECTOR_STORE_DIR = BASE_DIR / os.getenv("VECTOR_STORE_DIR", "chroma_db")
APP_ENV = os.getenv("APP_ENV", "development")
LLM_ENABLED = os.getenv("LLM_ENABLED", "false").lower() == "true"
