![Screenshot 2024-11-14 223034](https://github.com/user-attachments/assets/77e4eb8f-56b9-4f9b-81f4-fb0e54374bcc)![Screenshot 2024-11-14 223034](https://github.com/user-attachments/assets/0a1b2428-a87b-4573-b015-6d9f568e91fc)


---

## **Project Overview**
The **Malayalam Grammar Checker** is a language processing tool designed to detect and correct grammatical errors in Malayalam text. It utilizes two key models:
1. **IndicBERT** for binary classification of grammatical correctness.
2. **MT5-Small** for grammatical error correction (GEC).

The frontend is built with **React.js**, providing a user-friendly interface, while the backend leverages **Flask** for model integration and processing.

---

## **Features**
- Detects if a given Malayalam sentence or paragraph contains grammatical errors.
- Highlights incorrect sections in red.
- Corrects the identified grammatical errors using a transformer-based GEC model.
- Displays corrected text with highlighting for user understanding.

---

## **System Requirements**
- **Python**: 3.8 or later
- **Node.js**: 16.x or later
- **React.js**
- **Required Python Libraries**:
  - `transformers`
  - `torch`
  - `flask`
  - `datasets`
  - `scikit-learn`
  - `pandas`

---

## **Setup Instructions**

### **1. Backend (Flask)**

#### **Set Up Environment**
- Create a virtual environment:
  ```bash
  python -m venv env
- On windows
  ```bash
  .\env\Scripts\activate
### **Install Required Libraries**
- pip install transformers torch flask datasets scikit-learn pandas

### **IndicBERT Model for Binary Classification**
- Model Details: IndicBERT is a multilingual transformer-based model specifically optimized for Indian languages, including Malayalam.
- Fine-tuning Steps:
- Load the pretrained IndicBERT model using the transformers library.
- Fine-tune the model on a labeled dataset of correct (1) and incorrect (0) sentences.
- Save the trained model:
- ```bash
  model.save_pretrained("./indic_bert_model")
  tokenizer.save_pretrained("./indic_bert_model")


### **MT5-Small Model for GEC**
- Model Details: MT5-Small is a multilingual text-to-text transformer used for generating corrected sentences.
- Fine-tuning Steps:
- Prepare a parallel corpus of incorrect and corrected Malayalam sentences.
- Fine-tune the MT5-Small model using this dataset.
- Save the trained model:
- ```bash
   model.save_pretrained("./gec_mt5_model")
   tokenizer.save_pretrained("./gec_mt5_model")


## **Project Workflow**

1. **Input**:
   - The user provides a Malayalam sentence or paragraph through the React.js frontend interface.

2. **Error Detection**:
   - The input text is sent to the Flask backend.
   - The **IndicBERT model** is used to classify the text into two categories: **correct** or **incorrect**.

3. **Error Correction**:
   - If the **IndicBERT model** detects errors, the **MT5-Small model** is invoked to generate a grammatically corrected version of the text.
   - The MT5-Small model is trained for **Grammatical Error Correction (GEC)** and uses the incorrect sentence to produce a corrected version.

4. **Output**:
   - The backend sends back the corrected text to the frontend.
   - In the React app, the errors are highlighted in **red** within the original text, and the corrected version of the sentence is shown alongside it.

