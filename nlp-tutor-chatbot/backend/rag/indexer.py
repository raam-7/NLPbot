from pathlib import Path
import pickle
import sys

import faiss
import numpy as np

# Allow direct execution: `python rag/indexer.py`
backend_root = Path(__file__).resolve().parent.parent
if str(backend_root) not in sys.path:
    sys.path.insert(0, str(backend_root))

from rag.loader import DocumentLoader
from rag.splitter import DocumentSplitter
from rag.embedder import EmbeddingGenerator


class VectorIndexer:
    """
    Builds and saves the FAISS vector index.
    """

    def __init__(self):
        project_root = Path(__file__).resolve().parent.parent.parent

        self.knowledge_base = project_root / "knowledge-base"
        self.vector_db = project_root / "vector-db"

        self.vector_db.mkdir(exist_ok=True)

        self.loader = DocumentLoader(self.knowledge_base)
        self.splitter = DocumentSplitter()
        self.embedder = EmbeddingGenerator()

    def build(self):

        print("\nLoading documents...")
        documents = self.loader.load_documents()

        print(f"Loaded {len(documents)} documents")

        print("\nSplitting documents...")
        chunks = self.splitter.split_documents(documents)

        print(f"Generated {len(chunks)} chunks")

        if len(chunks) == 0:
            print("\nNo chunks found.")
            print("Populate your knowledge-base first.")
            return

        print("\nGenerating embeddings...")

        embeddings = self.embedder.embed_documents(chunks)

        embeddings = np.array(
            embeddings,
            dtype="float32"
        )

        dimension = embeddings.shape[1]

        print(f"Embedding Dimension : {dimension}")

        index = faiss.IndexFlatL2(dimension)

        index.add(embeddings)

        faiss.write_index(
            index,
            str(self.vector_db / "index.faiss")
        )

        with open(
            self.vector_db / "metadata.pkl",
            "wb",
        ) as f:
            pickle.dump(chunks, f)

        print("\n" + "=" * 60)
        print("FAISS Index Created Successfully!")
        print("=" * 60)

        print(f"Vectors Stored : {index.ntotal}")


if __name__ == "__main__":
    indexer = VectorIndexer()
    indexer.build()
