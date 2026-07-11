from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
KB_ROOT = PROJECT_ROOT / "knowledge-base"

KB_STRUCTURE = {
    "basics": [
        "introduction.md",
        "history.md",
        "nlp_pipeline.md",
        "applications.md",
    ],
    "preprocessing": [
        "text_cleaning.md",
        "tokenization.md",
        "stemming.md",
        "lemmatization.md",
        "stop_words.md",
        "regex.md",
        "sentence_segmentation.md",
    ],
    "syntax": [
        "pos_tagging.md",
        "dependency_parsing.md",
        "named_entity_recognition.md",
        "chunking.md",
        "parsing.md",
    ],
    "embeddings": [
        "word_embeddings.md",
        "word2vec.md",
        "glove.md",
        "fasttext.md",
        "tf.md",
        "idf.md",
        "tfidf.md",
        "bag_of_words.md",
        "ngrames.md",
    ],
    "transformers": [
        "transformer.md",
        "self_attention.md",
        "multi_head_attention.md",
        "encoder.md",
        "decoder.md",
        "bert.md",
        "gpt.md",
        "prompt_engineering.md",
    ],
    "llms": [
        "embeddings.md",
        "faiss.md",
        "rag.md",
        "vector_database.md",
        "recent_llm_concepts.md",
    ],
    "evaluation": [
        "accuracy.md",
        "precision.md",
        "recall.md",
        "f1_score.md",
        "bleu.md",
        "rouge.md",
        "confusion_matrix.md",
    ],
    "applications": [
        "chatbots.md",
        "question_answering.md",
        "machine_translation.md",
        "information_retrieval.md",
        "sentiment_analysis.md",
        "text_classification.md",
        "topic_modeling.md",
    ],
}


def ensure_kb_structure() -> list[Path]:
    created_paths: list[Path] = []

    for category, filenames in KB_STRUCTURE.items():
        category_dir = KB_ROOT / category
        category_dir.mkdir(parents=True, exist_ok=True)

        for filename in filenames:
            file_path = category_dir / filename
            if not file_path.exists():
                file_path.touch()
                created_paths.append(file_path)

    return created_paths


def main() -> None:
    created_paths = ensure_kb_structure()

    if not created_paths:
        print("Knowledge base structure already exists. Nothing to create.")
        return

    print("Created missing knowledge base files:")
    for path in created_paths:
        print(f"- {path.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
