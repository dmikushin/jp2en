# Japanese to English NLP-based translation service

Translate Japanese text to English text offline from the command line, using the NLP model published by [tommy19970714](https://huggingface.co/tommy19970714/translation-japanese).

| testset       | BLEU | chr-F |
| ------------- | ---- | ----- |
| Tatoeba.ja.en | 41.7 | 0.589 |

The quality of translation is acceptable in practice: a translation of a technical book in Japanese is easy to follow.

## Prerequisites

Clone the repository recursively with the Git LFS enabled:

```
git lfs install
git clone --recurse-submodules https://github.com/dmikushin/jp2en.git
```

Prepare Python virtual environment:

```
python3 -m venv ./venv
./venv/bin/activate
pip3 install wheel transformers torch sentencepiece python-socketio aiohttp
```

## Usage

Start the server:

```
python ./jp2en_server
```

Execute the client:

```
python ./jp2en "ADC ファイルが作られると，TD の左側にある「Hierarchy Navigation」メニューの 「Project」タブの中に「io.adc」ファイルが表示されます.この ADC ファイルを開くと，端 子の設定がテキストで書かれていることがわかります.このファイルを直接書き換えることで
も端子の設定を行うことができます."
When a DCC file is created, the "O. Adc" file will be displayed in the "Healerch Navigation" tab on the left side of the TDTD. If you open this ADC file, you will find that the settings of the terminals are written in text. You can also set them by making this file read directly.
```

