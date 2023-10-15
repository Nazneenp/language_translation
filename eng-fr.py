from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="torch.storage")

# Chargez le modèle T5 pré-entraîné pour la traduction anglais-français
model_name = "t5-base"
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Chargez le tokenizer associé
tokenizer = T5Tokenizer.from_pretrained(model_name)

def translate_english_to_french(english_sentence):
    # Préparez la phrase pour l'entrée du modèle (ajoutez le préfixe "translate English to French: ")
    input_text = "translate English to French: " + english_sentence

    # Tokenize la phrase et encode les tokens en IDs
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Générez la traduction en français
    with torch.no_grad():
        outputs = model.generate(input_ids=input_ids)

    # Décodage de la traduction en français à partir des IDs de tokens générés
    french_translation = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return french_translation

english_sentence = "Hello, how was your day ?"
french_translation = translate_english_to_french(english_sentence)

print("English:", english_sentence)
print("French:", french_translation)