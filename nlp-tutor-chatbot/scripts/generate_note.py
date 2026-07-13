from pathlib import Path

from ollama import chat

# =====================================================
# Configuration
# =====================================================

TOPIC = "Tokenization"

CATEGORY = "preprocessing"

OUTPUT_FILE = (
    Path(__file__).resolve().parent.parent
    / "knowledge-base"
    / CATEGORY
    / "tokenization.md"
)

PROMPT = f"""
You are an experienced university professor teaching Natural Language Processing.

Create COMPLETE study notes in Markdown on the topic:

{TOPIC}

Requirements:

# Title

## Definition

## Simple Explanation

## Why It Is Important

## Real World Analogy

## Real World Example

## Python Example (using nltk)

## Expected Output

## Applications

## Advantages

## Limitations

## Common Mistakes

## Interview Questions (5)

## Practice Questions (5)

## Summary

Rules:

- Write in simple English.
- Suitable for B.Tech AIML students.
- Use Markdown headings.
- Give proper Python code.
- Explain every section clearly.
- Minimum 1000 words.
"""

# =====================================================
# Generate Notes
# =====================================================

print("Generating notes...\n")

response = chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": PROMPT,
        }
    ],
)

content = response["message"]["content"]

OUTPUT_FILE.write_text(
    content,
    encoding="utf-8",
)

print("=" * 60)
print("Knowledge file generated successfully!")
print("=" * 60)
print(OUTPUT_FILE)