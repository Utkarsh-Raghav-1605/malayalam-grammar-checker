from transformers import MT5ForConditionalGeneration, MT5Tokenizer
import torch
import evaluate
import pandas as pd

# Specify the corrected path for the trained model
model_path = r'D:\malayalam_grammar_checker\GEC\gec_mt5_model'

# Load the model and tokenizer
model = MT5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = MT5Tokenizer.from_pretrained('google/mt5-small')

# Load the test dataset (e.g., a CSV file with columns 'incorrect_sentence' and 'corrected_sentence')
test_data_path = r'D:\malayalam_grammar_checker\GEC\validation-gec.csv'
df_test = pd.read_csv(test_data_path)

# Load BLEU score metric
bleu_metric = evaluate.load("bleu")

# Function to generate the corrected sentence
def generate_corrected_sentence(sentence):
    inputs = tokenizer(sentence, return_tensors="pt", padding='max_length', truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model.generate(inputs["input_ids"], max_length=128, num_beams=4, early_stopping=True)

    corrected_sentence = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected_sentence

# Apply the model on all test sentences
y_true = df_test['corrected_sentence'].tolist()  # Ground truth corrected sentences
y_pred = [generate_corrected_sentence(sentence) for sentence in df_test['incorrect_sentence'].tolist()]  # Model predictions

# Calculate BLEU score for the generated sentences
bleu_score = bleu_metric.compute(predictions=y_pred, references=[[label] for label in y_true])

# Print BLEU score
print(f"BLEU Score: {bleu_score}")
n= len(y_true)
# Optional: Print actual vs predicted sentences for manual inspection
for i, sentence in enumerate(df_test['incorrect_sentence'].tolist()):
    print(f"Incorrect Sentence: {sentence}")
    print(f"Actual Corrected Sentence: {y_true[i]}")
    print(f"Predicted Corrected Sentence: {y_pred[i]}\n")
