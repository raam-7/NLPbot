from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import HashingVectorizer

from core.config import settings

try:
    from sentence_transformers import SentenceTransformer
except Exception:  # pragma: no cover - optional dependency fallback
    SentenceTransformer = None


class EmbeddingGenerator:
    """
    Generates embeddings using Sentence Transformers.
    """

    def __init__(
        self,
        fallback_dimension: int = 384,
    ):
        print("Loading embedding model...")

        self.model = None
        self.vectorizer = None
        self.dimension = fallback_dimension

        model_name = settings.EMBEDDING_MODEL.strip()

        if SentenceTransformer is not None:
            try:
                model_path = Path(model_name)
                if model_path.exists():
                    self.model = SentenceTransformer(str(model_path))
                else:
                   self.model = SentenceTransformer(model_name)

                print("Model loaded successfully.")
                return

            except Exception as exc:
                print(
                    f"SentenceTransformer unavailable, using offline fallback: {exc}"
                )

        self.vectorizer = HashingVectorizer(
            n_features=self.dimension,
            alternate_sign=False,
            norm="l2",
            lowercase=True,
        )
        print("Offline hashing embedder loaded.")

    def embed_text(self, text: str):
        if self.model is not None:
            return self.model.encode(
                text,
                convert_to_numpy=True,
            )

        return self.vectorizer.transform([text]).toarray()[0].astype(
            np.float32
        )

    def embed_documents(
        self,
        chunks: list[dict],
    ):

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        if self.model is not None:
            return self.model.encode(
                texts,
                convert_to_numpy=True,
                show_progress_bar=True,
            )

        return self.vectorizer.transform(texts).toarray().astype(
            np.float32
        )
