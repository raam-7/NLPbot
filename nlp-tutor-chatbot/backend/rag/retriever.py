from pathlib import Path
import pickle

import faiss

from rag.embedder import EmbeddingGenerator


class Retriever:
    """
    Retrieves the most relevant chunks from the selected FAISS index.
    """

    def __init__(self, kb_type: str):
        """
        Initialize the retriever.

        Args:
            kb_type: "theory" or "practical"
        """

        self.kb_type = kb_type

        project_root = Path(__file__).resolve().parent.parent.parent

        vector_db = (
            project_root
            / "backend"
            / "vector-db"
            / kb_type
        )

        index_path = vector_db / "index.faiss"
        metadata_path = vector_db / "metadata.pkl"

        if not index_path.exists():
            raise FileNotFoundError(
                f"FAISS index not found:\n{index_path}"
            )

        if not metadata_path.exists():
            raise FileNotFoundError(
                f"Metadata file not found:\n{metadata_path}"
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
        """
        Search the FAISS index.
        """

        query_vector = self.embedder.embed_text(query)

        distances, indices = self.index.search(
            query_vector.reshape(1, -1),
            top_k,
        )

        results = []

        for i in range(len(indices[0])):

            idx = indices[0][i]

            if idx == -1:
                continue

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

    kb_type = input(
        "Knowledge Base (theory/practical): "
    ).strip().lower()

    if kb_type not in ["theory", "practical"]:
        print("Invalid knowledge base.")
        raise SystemExit(1)

    retriever = Retriever(kb_type)

    query = input("Ask a question: ")

    results = retriever.search(query)

    print("\n")
    print("=" * 70)
    print("Retrieved Chunks")
    print("=" * 70)

    for result in results:

        print(f"\nTitle    : {result['title']}")
        print(f"Source   : {result['source']}")
        print(f"Distance : {result['score']:.4f}\n")

        print(result["text"][:400])

        print("-" * 70)