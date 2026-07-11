from pathlib import Path
from typing import List


class DocumentLoader:
    """
    Loads Markdown files from the knowledge base.
    """

    def __init__(self, knowledge_base_path: str):
        self.knowledge_base_path = Path(knowledge_base_path)

    def load_documents(self) -> List[dict]:
        """
        Read all Markdown files recursively.
        """

        documents = []

        for file in self.knowledge_base_path.rglob("*.md"):

            text = file.read_text(
                encoding="utf-8"
            )

            documents.append(
                {
                    "title": file.stem.replace("_", " ").title(),
                    "text": text,
                    "source": str(
                        file.relative_to(
                            self.knowledge_base_path
                        )
                    ),
                }
            )

        return documents


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent.parent
    knowledge_base = project_root / "knowledge-base"

    loader = DocumentLoader(knowledge_base)

    docs = loader.load_documents()

    print("=" * 60)
    print(f"Knowledge Base Path: {knowledge_base}")
    print(f"Loaded {len(docs)} documents")
    print("=" * 60)

    for doc in docs[:5]:
        print(doc["title"])
        print(doc["source"])
        print("-" * 40)