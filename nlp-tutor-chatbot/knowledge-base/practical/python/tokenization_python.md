# Tokenization in Python using NLTK

## Objective

Learn how to perform tokenization using Python and the NLTK library.

---

## Install NLTK

```bash
pip install nltk
```

---

## Python Code

```python
import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer (run once)
nltk.download("punkt")

text = "Natural Language Processing is amazing!"

tokens = word_tokenize(text)

print(tokens)
```

---

## Expected Output

```text
['Natural', 'Language', 'Processing', 'is', 'amazing', '!']
```

---

## Explanation

- Import the `word_tokenize` function.
- Download the tokenizer data using `nltk.download("punkt")`.
- Pass the input string to `word_tokenize()`.
- The function returns a list of tokens.

---

## Best Practices

- Download `punkt` only once.
- Always preprocess text before tokenization if required.
- Use language-specific tokenizers for multilingual applications.

---

## Common Interview Question

**Q:** Why do we tokenize text?

**Answer:** Tokenization converts raw text into smaller units that machine learning models can process efficiently.