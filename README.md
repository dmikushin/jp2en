# Japanese to English NLP-based translation service

Translate Japanese text to English text using the NLP model is published by [tommy19970714](https://huggingface.co/tommy19970714/translation-japanese).

| testset       | BLEU | chr-F |
| ------------- | ---- | ----- |
| Tatoeba.ja.en | 41.7 | 0.589 |

The quality of translation is acceptable in practice: a translation of a technical book in Japanese is easy to follow.

## Prerequisites

```
python3 -m venv ./venv
./venv/bin/activate
pip3 install transformers torch sentencepiece
```

## Usage

```
python ./jp2en.py
```

