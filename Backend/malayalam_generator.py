import random
import pandas as pd

# Sample base sentences for generating data
base_sentences = [
    "ഞാൻ പുസ്തകം വായിക്കുന്നു.",  # Correct
    "അവൻ സ്കൂളിലേക്ക് പോകുന്നു.",  # Incorrect
    "അവളുടെ പേര് റാധികയാണ്.",  # Correct
    "നാം പുഴയിൽ നീന്തുന്നു.",  # Correct
    "അവരവൻ തുണി ധരിച്ചിരിക്കുന്നു.",  # Incorrect
    "എനിക്ക് പന്ത് കഴിക്കണം.",  # Correct
    "അവൻ കായിക പ്രവർത്തനങ്ങൾ നടത്തുന്നു.",  # Correct
    "ഞങ്ങൾ വാരാന്ത്യത്തിൽ യാത്ര പോകുന്നു.",  # Correct
    "അവളുടെ സന്തോഷം എന്റെ സന്തോഷമാണ്.",  # Incorrect
    "അവൻ വീട്ടിലേക്കു വരുന്നു."   # Correct
]

# Function to generate sentences with labels
def generate_dataset(num_samples):
    dataset = []
    for _ in range(num_samples):
        # Decide randomly to create a correct or incorrect sentence
        if random.random() < 0.7:  # 70% chance for correct sentences
            base_sentence = random.choice(base_sentences)
            label = 1
        else:
            # Create a simple incorrect variation
            base_sentence = random.choice(base_sentences)
            incorrect_sentence = base_sentence.replace("ഞാൻ", "ഞാനെ")  # Example of incorrect modification
            base_sentence = incorrect_sentence
            label = 0

        dataset.append((base_sentence, label))
    
    return dataset

# Generate dataset with over 1000 entries
dataset_size = 1200
dataset = generate_dataset(dataset_size)

# Save to CSV
df = pd.DataFrame(dataset, columns=["Sentences", "Label"])
df.to_csv("malayalam_grammar_dataset.csv", index=False)

print(f"Generated a dataset with {len(dataset)} sentences and saved to 'malayalam_grammar_dataset.csv'")
