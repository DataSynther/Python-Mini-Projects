
# End-to-End Chatbot using Python and Streamlit

This project demonstrates the implementation of an end-to-end chatbot using Python, Natural Language Processing (NLP), and Streamlit for the user interface.

## 🧠 What is a Chatbot?

A chatbot is a computer program designed to simulate conversation with human users. It uses Natural Language Processing (NLP) to understand queries and respond with meaningful answers.

This chatbot can handle full conversations without human assistance once deployed.

---

## 🚀 Project Workflow

To build this chatbot, we follow these steps:

1. **Define Intents**
2. **Create Training Data**
3. **Train the Chatbot**
4. **Build the Chatbot Logic**
5. **Test the Chatbot**
6. **Deploy with Streamlit**

---

## 🛠️ Features

- Handles greetings, goodbyes, and common queries.
- Supports queries on budgeting, credit scores, and more.
- Simple NLP using `TfidfVectorizer` and `LogisticRegression`.
- Interactive interface using Streamlit.

---

## 📦 Requirements

Install the following Python libraries before running:

```bash
pip install streamlit scikit-learn nltk
```

---

## 💡 How to Run

```bash
streamlit run chatbot.py
```

---

## 📁 Folder Structure

```
chatbot_project/
├── chatbot.py
├── nltk_data/              # Optional: For offline nltk resources
└── README.md
```

---

## ⚠️ Notes

- SSL verification is disabled for downloading nltk resources (not recommended for production).
- Streamlit's `st.text_input()` is used for input and `st.text_area()` for responses.
- The chatbot does **not** support real-time data (like weather or external APIs).

---

## 🤖 Sample Intents Covered

- Greetings
- Farewells
- Help requests
- Age inquiries
- Budgeting advice
- Credit score queries

---

## 🙌 Author

Built with ❤️ by Sam.
