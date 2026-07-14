import uvicorn

from retrieval.retrieval import rebuild_index


def main() -> None:
    chunks = rebuild_index()
    print(f"Indexed {chunks} sample document chunks.")
    print("Run the API with: uvicorn app.main:app --reload")


if __name__ == "__main__":
    main()
