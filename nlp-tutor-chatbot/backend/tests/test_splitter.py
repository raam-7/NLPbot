from pathlib import Path
import sys

backend_root = Path(__file__).resolve().parent.parent
if str(backend_root) not in sys.path:
    sys.path.insert(0, str(backend_root))

from rag.loader import DocumentLoader
from rag.splitter import DocumentSplitter


project_root = Path(__file__).resolve().parent.parent.parent
knowledge_base = project_root / "knowledge-base"

loader = DocumentLoader(knowledge_base)
documents = loader.load_documents()

splitter = DocumentSplitter()

chunks = splitter.split_documents(documents)

print("=" * 60)
print(f"Documents : {len(documents)}")
print(f"Chunks    : {len(chunks)}")
print("=" * 60)

if not documents:
    print("No knowledge base documents were loaded.")
    raise SystemExit(0)

print(f"Documents: {len(documents)}")
print(f"First document title: {documents[0]['title']}")
print(f"Text length: {len(documents[0]['text'])}")
print(documents[0]['text'][:200])

if not chunks:
    print("No chunks were generated because the source documents are empty.")
    raise SystemExit(0)

print(f"Chunks: {len(chunks)}")
print(f"First chunk title: {chunks[0]['title']}")
print(f"First chunk text: {chunks[0]['text'][:200]}")
