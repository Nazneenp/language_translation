from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="torch.storage")

# Load the model and tokenizer for the new language (German in this example)
model_name = "t5-small"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

def translate_to_new_language(input_sentence):
    input_text = f"translate English to German: {input_sentence}"  # Change the target language accordingly
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(input_ids=input_ids)

    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return translated_text

input_sentence = "Hello, how are you?"
translated_sentence = translate_to_new_language(input_sentence)

print("Input:", input_sentence)
print("Translation:", translated_sentence)