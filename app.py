from flask import Flask, render_template, request

app = Flask(__name__)

from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="torch.storage")

# Load the models and tokenizers for both French and German translations
french_model_name = "t5-base"
french_model = T5ForConditionalGeneration.from_pretrained(french_model_name)
french_tokenizer = T5Tokenizer.from_pretrained(french_model_name)

german_model_name = "t5-small"
german_model = T5ForConditionalGeneration.from_pretrained(german_model_name)
german_tokenizer = T5Tokenizer.from_pretrained(german_model_name)

def translate_to_language(input_sentence, target_language):
    if target_language == "French":
        model = french_model
        tokenizer = french_tokenizer
        translation_prefix = "translate English to French: "
    elif target_language == "German":
        model = german_model
        tokenizer = german_tokenizer
        translation_prefix = "translate English to German: "
    else:
        return "Unsupported language"

    input_text = translation_prefix + input_sentence
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(input_ids=input_ids)

    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return translated_text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    if request.method == "POST":
        input_sentence = request.form["input_sentence"]
        target_language = request.form["target_language"]

        translation = translate_to_language(input_sentence, target_language)

        return render_template("result.html", input_sentence=input_sentence, target_language=target_language, translation=translation)

if __name__ == "__main__":
    app.run(debug=True)
