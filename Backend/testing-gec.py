from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
# Specify the corrected path
model_path = r'D:\malayalam_grammar_checker\grammarChecker\results\checkpoint-224'

model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained('ai4bharat/indic-bert')

# Load the test dataset (e.g., a CSV file with columns 'text' and 'label')
test_data_path = r'D:\malayalam_grammar_checker\grammarChecker\check_data.csv'
df_test = pd.read_csv(test_data_path)

# Function to predict the label (correct or incorrect) for a given sentence
def predict_label(sentence):
    inputs = tokenizer(sentence, padding='max_length', truncation=True, max_length=128, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return predicted_class

# Apply the model on all test sentences
y_true = df_test['label'].tolist()  # Actual labels from the dataset (1 for correct, 0 for incorrect)
y_pred = [predict_label(sentence) for sentence in df_test['text'].tolist()]  # Model predictions

# Calculate classification metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

# Print results
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")

# Optional: Print actual vs predicted labels for manual inspection
for i, sentence in enumerate(df_test['text'].tolist()):
    print(f"Sentence: {sentence}")
    print(f"Actual Label: {y_true[i]}, Predicted Label: {y_pred[i]}\n")