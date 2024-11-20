from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, MT5ForConditionalGeneration

app = Flask(__name__)
CORS(app)

# Load models
classification_model = AutoModelForSequenceClassification.from_pretrained("D:/PROJECTS/malayalam_grammar_checker/grammarChecker/results/checkpoint-224")
classification_tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indic-bert")
gec_model = MT5ForConditionalGeneration.from_pretrained("D:/malayalam_grammar_checker/GEC/gec_mt5_model")
gec_tokenizer = AutoTokenizer.from_pretrained("google/mt5-small")

# Function to get predictions from Indic-BERT model
def test_model(sentence):
    inputs = classification_tokenizer(sentence, padding="max_length", truncation=True, max_length=128, return_tensors="pt")
    with torch.no_grad():
        outputs = classification_model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return predicted_class

# Function to get corrected paragraph using mt5 model
def get_corrected_paragraph(sentence):
    inputs = gec_tokenizer.encode(sentence, return_tensors="pt", max_length=128, truncation=True)
    with torch.no_grad():
        outputs = gec_model.generate(inputs, max_length=128, num_beams=5, early_stopping=True)
    corrected_paragraph = gec_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected_paragraph

@app.route("/check", methods=["POST"])
def check_sentence():
    data = request.json
    sentence = data.get("sentence")
    pred_label = test_model(sentence)
    
    if pred_label == 1:  # Sentence is correct
        response = {
            "sentence": sentence,
            "prediction": "Correct",
            "corrected_paragraph": sentence
        }
    else:  # Sentence is incorrect, fetch corrected paragraph from mt5 model
        corrected_paragraph = get_corrected_paragraph(sentence)
        response = {
            "sentence": sentence,
            "prediction": "Incorrect",
            "corrected_paragraph": corrected_paragraph
        }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
