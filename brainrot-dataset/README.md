# Brainrot Dataset

A parallel corpus for translating standard English to "brainrot" internet language style.

## Description

This dataset contains pairs of English sentences and their corresponding "brainrot" style translations. The brainrot style is characterized by:

- Casual, conversational language
- Heavy use of emojis
- Lowercase text
- Internet slang like "fr" (for real), "tryna" (trying to)
- References to "king/queen"
- Exaggerated expressions
- Prayer hands emoji (🙏)
- Minimalist punctuation

The dataset is suitable for training sequence-to-sequence models that can transform formal/standard English into this distinctive internet language style.

## Dataset Structure

### Data Instances

Each instance in the dataset consists of:
- `source`: The original English text in standard style
- `target`: The corresponding text in "brainrot" style

Example:
```json
{
  "source": "I am very tired today",
  "target": "bro i'm running on vibes and resentment rn"
}
```

### Data Fields

- `source`: A string containing the original English text
- `target`: A string containing the transformed "brainrot" style text

### Data Splits

The dataset is divided into three splits:

- Train: 5,664 examples
- Validation: 503 examples
- Test: 508 examples

## Usage

You can load this dataset using the Hugging Face `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("your-username/brainrot-dataset")

# Access specific splits
train_data = dataset["train"]
validation_data = dataset["validation"]
test_data = dataset["test"]

# Example usage
for example in train_data.select(range(5)):
    print(f"Source: {example['source']}")
    print(f"Target: {example['target']}")
    print("-" * 50)
```

## Intended Uses

This dataset can be used for:

1. Training sequence-to-sequence models for text style transfer
2. Studying internet language patterns and evolution
3. Creating content generators that can produce text in this specific internet style
4. Analyzing the linguistic features of internet slang and casual communication

## Limitations

1. The dataset primarily focuses on a specific internet language style and may not represent the full diversity of internet language
2. Some translations may contain slang that could become outdated as internet language evolves
3. The dataset is in English only

## Citation

If you use this dataset in your research, please cite:

```
@misc{brainrot-dataset,
  author = {Shiven},
  title = {Brainrot Dataset: A Corpus for English to Internet Slang Translation},
  year = {2025},
  howpublished = {\url{https://huggingface.co/datasets/shvn22k/brainrot-dataset}}
}
```
