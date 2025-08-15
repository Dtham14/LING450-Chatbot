# Conversational AI with ChatterBot

A Python-based chatbot built with the [ChatterBot](https://chatterbot.readthedocs.io/en/stable/) library, trained on a large conversational dataset from Kaggle. This project was developed as part of the **LING 450 – Spring 2024** course to explore the implementation, customization, and evaluation of corpus-based chatbots.

---

## 📌 Overview

With the rise of AI-driven conversational tools like ChatGPT, chatbots have become a common part of everyday life — from banking assistants to voice-activated home devices. This project investigates **corpus-based, retrieval-style chatbots** using ChatterBot, focusing on:

- How conversational datasets can be processed and used for training.
- Customizing chatbot personality and responses.
- Evaluating conversational relevance and coherence.

The end goal: create a chatbot capable of engaging in casual, human-like conversation using a large topical chat dataset.

---

## 🛠 Features

- **Corpus-Based Retrieval Architecture** – Uses a dataset of over 184,000 messages to provide relevant responses.
- **Custom Preprocessing** – Cleans and formats raw CSV data for effective training.
- **Logic Adapters** – Implements ChatterBot’s `BestMatch` logic with tuned similarity thresholds.
- **Personality Layer** – Appends custom phrases based on punctuation in user input for a more human-like feel.
- **Extensible Modules** – Potential for additional logic adapters, sentiment analysis, and UI integration.

---

## 📂 Dataset

- **Source:** [Kaggle – Chatbot Dataset Topical Chat](https://www.kaggle.com/datasets/arnavsharmaas/chatbot-dataset-topical-chat) by Arnav Sharma  
- **Size:** ~8,000 conversations, ~184,000 messages.
- **Fields:**  
  - Conversation ID  
  - Message text  
  - Sentiment label (8 categories, not used in this version)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Dtham14/LING450-Chatbot.git
cd LING450-Chatbot
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### 3️⃣ Install Requirements
```bash
python -m pip install chatterbot==1.0.4 pytz
```
> **Note:** The standard `pip install chatterbot` may not work due to compatibility issues. The above command follows [Real Python’s guide](https://realpython.com/build-a-chatbot-python-chatterbot/).

### 4️⃣ Run the Chatbot
```bash
python chatbot.py
```

---

## 🧠 How It Works

### **Architecture**
- **ChatterBot** uses a **corpus-based, response-by-retrieval** approach.
- Incoming text is processed into a **graph-like structure**.
- A **Naive Bayes classifier** helps determine the most relevant response.

### **Training**
- Data is loaded using **ListTrainer**, which accepts an array of cleaned conversation pairs.
- A similarity threshold (`maximum_similarity_threshold`) of **0.70** was chosen to balance relevance and avoid dead-end responses.

### **Personality Enhancements**
- Checks punctuation in user input:
  - Question marks trigger thoughtful prefaces (`"Hmm..."`)
  - Exclamation marks trigger excited responses (`"Wow!"`, `"Of course!"`)
- Mimics conversational flow seen in advanced chatbots like ChatGPT.

---

## 🚧 Challenges

- **Data Formatting Issues** – Some messages in the dataset contained inconsistent quotation marks requiring multiple preprocessing passes.
- **Memory Usage** – Training on the full dataset initially caused memory errors when each character was parsed individually instead of whole sentences.
- **Adapter Limitations** – Built-in corpora failed to run on the development machine, requiring reliance on `ListTrainer`.

---

## 📊 Evaluation

The chatbot performs well in:
- Standard greetings.
- Following certain conversational chains.

However, limitations include:
- Occasional topic drift.
- Lack of deep contextual understanding.
- Irrelevant matches when dataset coverage is low.

Example:
> **User:** "Do you like Steph Curry?"  
> **Bot:** "Does it smell good?" *(linked "Curry" to food-related message in dataset)*

---

## 🔮 Future Improvements

- **Web Interface** – A ChatGPT-style UI with an input field and scrollable conversation history.
- **Noun-Based Relevance Filtering** – Use [spaCy](https://spacy.io/) to detect key nouns in input and bias responses containing those nouns.
- **Sentiment Awareness** – Incorporate sentiment column from dataset to adjust tone.
- **Expanded Training Data** – Merge multiple large-scale datasets for better coverage.

---

## 📚 References

- Arnav Sharma. [Chatbot Dataset Topical Chat – Kaggle](https://www.kaggle.com/datasets/arnavsharmaas/chatbot-dataset-topical-chat)  
- [ChatterBot Documentation](https://chatterbot.readthedocs.io/en/stable/)  
- [Real Python – Build a Chatbot with Python](https://realpython.com/build-a-chatbot-python-chatterbot/)  
- Taboada, Maite. *Applications: Chatbots & Dialogue Agents.* Lecture slides, April 11, 2024.

---

## 👤 Author

**Daniel Tham**  
GitHub: [@Dtham14](https://github.com/Dtham14)

---
```  

Do you want me to also **add diagrams** to visually explain the architecture and workflow for this README so it looks more professional on GitHub?  
That could make it stand out more to recruiters and project viewers.
