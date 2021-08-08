from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Suppress "UserWarning: floor_divide is deprecated"
import warnings
warnings.filterwarnings("ignore")

tokenizer = AutoTokenizer.from_pretrained("./ThirdParty/translation-japanese")

model = AutoModelForSeq2SeqLM.from_pretrained("./ThirdParty/translation-japanese")

text = "こんにちは！テキスト入力は提供されていません。"

translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
for t in translated :
    print(tokenizer.decode(t, skip_special_tokens=True))
