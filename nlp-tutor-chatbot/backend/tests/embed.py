from rag.embedder import EmbeddingGenerator

embedder = EmbeddingGenerator()

text = "Tokenization is the process of splitting text into tokens."

vector = embedder.embed_text(text)

print("=" * 60)
print("Embedding Generated Successfully")
print("=" * 60)

print("Vector Length :", len(vector))

print("\nFirst 10 Values:\n")

print(vector[:10])