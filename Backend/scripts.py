from datasets import load_dataset
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
dataset = load_dataset('csv', data_files={
    'train': r'D:\grammarChecker\malayalam_grammar_dataset.csv',
    'test': r'D:\grammarChecker\check_data.csv'
}, delimiter=',')

# Load the tokenizer for IndicBERT (pre-trained for Indian languages)
tokenizer = AutoTokenizer.from_pretrained('ai4bharat/indic-bert')

# Define the preprocessing function
def preprocess_function(examples):
    # Tokenize the input sentences, with padding and truncation to a max length (e.g., 128 tokens)
    return tokenizer(examples['text'], padding='max_length', truncation=True, max_length=128)

# Apply the preprocessing function to the dataset
# It will process both train and test splits
tokenized_datasets = dataset.map(preprocess_function, batched=True)

# Print a sample to ensure preprocessing worked
print(tokenized_datasets['train'][0])


model = AutoModelForSequenceClassification.from_pretrained('ai4bharat/indic-bert', num_labels=2)


training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy="epoch",
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=7,  # Try more epochs
    logging_dir='./logs',
    logging_steps=10,
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['test'],
)

# Train the model
trainer.train()
