from pathlib import Path
import pickle
import sys

import faiss
import numpy as np

# Allow direct execution: `python -m rag.indexer`
backend_root = Path(__file__).resolve().parent.parent
if str(backend_root) not in sys.path:
    sys.path.insert(0, str(backend_root))

from rag.embedder import EmbeddingGenerator
from rag.loader import DocumentLoader
from rag.splitter import DocumentSplitter


class VectorIndexer:
    """
    Builds and saves the FAISS vector index for a knowledge-base type.
    """

    def __init__(self, kb_type: str = "theory"):
        self.kb_type = kb_type.strip().lower()

        if self.kb_type not in {"theory", "practical"}:
            raise ValueError("kb_type must be 'theory' or 'practical'")

        project_root = Path(__file__).resolve().parent.parent.parent

        self.knowledge_base = project_root / "knowledge-base" / self.kb_type
        if not self.knowledge_base.exists():
            raise FileNotFoundError(
                f"Knowledge base '{self.kb_type}' not found at:\n{self.knowledge_base}"
            )

        self.vector_db = project_root / "backend" / "vector-db" / self.kb_type
        self.vector_db.mkdir(parents=True, exist_ok=True)

        self.loader = DocumentLoader(self.knowledge_base)
        self.splitter = DocumentSplitter()
        self.embedder = EmbeddingGenerator()

    def build_index(self) -> None:
        self.build()

    def build(self) -> None:
        print("\nLoading documents...")
        documents = self.loader.load_documents()
        print(f"Loaded {len(documents)} documents")

        print("\nSplitting documents...")
        chunks = self.splitter.split_documents(documents)
        print(f"Generated {len(chunks)} chunks")

        if not chunks:
            print("\nNo chunks found.")
            print("Populate your knowledge-base first.")
            return

        print("\nGenerating embeddings...")
        embeddings = self.embedder.embed_documents(chunks)

        embeddings = np.array(embeddings, dtype="float32")
        dimension = embeddings.shape[1]
        print(f"Embedding Dimension : {dimension}")

        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)

        faiss.write_index(index, str(self.vector_db / "index.faiss"))

        with open(self.vector_db / "metadata.pkl", "wb") as f:
            pickle.dump(chunks, f)

        print("\n" + "=" * 60)
        print("FAISS Index Created Successfully!")
        print("=" * 60)
        print(f"Vectors Stored : {index.ntotal}")


if __name__ == "__main__":
    kb_type = input("Build which knowledge base (theory/practical): ").strip().lower()

    if kb_type not in {"theory", "practical"}:
        print("Invalid knowledge base.")
        print("Choose either 'theory' or 'practical'.")
        raise SystemExit(1)

    indexer = VectorIndexer(kb_type)
    indexer.build_index()
