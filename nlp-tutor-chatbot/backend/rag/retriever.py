from pathlib import Path
import pickle
import sys

import faiss

from rag.embedder import EmbeddingGenerator


class Retriever:
    """
    Retrieves the most relevant chunks from the FAISS index.
    """

    def __init__(self):
        project_root = Path(__file__).resolve().parent.parent.parent

        vector_db = project_root / "vector-db"
        index_path = vector_db / "index.faiss"
        metadata_path = vector_db / "metadata.pkl"

        if not index_path.exists() or not metadata_path.exists():
            raise FileNotFoundError(
                "FAISS index files are missing. Run `python rag/indexer.py` "
                "from the backend directory after building the knowledge base."
            )

        self.index = faiss.read_index(
            str(index_path)
        )

        with open(metadata_path, "rb") as f:
            self.metadata = pickle.load(f)

        self.embedder = EmbeddingGenerator()

    def search(
        self,
        query: str,
        top_k: int = 5,
    ):

        query_vector = self.embedder.embed_text(query)

        distances, indices = self.index.search(
            query_vector.reshape(1, -1),
            top_k,
        )

        results = []

        for i in range(len(indices[0])):

            idx = indices[0][i]

            results.append(
                {
                    "score": float(distances[0][i]),
                    "title": self.metadata[idx]["title"],
                    "source": self.metadata[idx]["source"],
                    "text": self.metadata[idx]["text"],
                }
            )

        return results


if __name__ == "__main__":

    retriever = Retriever()

    try:
        query = input("Ask a question: ")
    except EOFError:
        print("No query provided. Run this module interactively to search the index.")
        raise SystemExit(0)

    results = retriever.search(query)

    print("\n")

    print("=" * 70)

    print("Retrieved Chunks")

    print("=" * 70)

    for result in results:

        print("\nTitle :", result["title"])

        print("Source:", result["source"])

        print("Distance:", result["score"])

        print()

        print(result["text"][:400])

        print("-" * 70)
