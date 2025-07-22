"""
A chatbot is a computer program that understands the intent of your query to answer with a solution. 
Chatbots are the most popular applications of Natural Language Processing in the industry.
An end-to-end chatbot refers to a chatbot that can handle a complete conversation from start to finish without requiring human assistance.
Once deployed, users can interact with the chatbot by sending it multiple requests and the chatbot can handle the entire conversation itself. 

To create an end-to-end chatbot using Python, we will follow the steps mentioned below:

- Define Intents
- Create training data
- Train the chatbot
- Build the chatbot
- Test the chatbot
- Deploy the chatbot

"""

# Importing necessary libraries
import os
import nltk
import ssl 
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1. Disable SSL verification (not recommended in production)
ssl._create_default_https_context = ssl._create_unverified_context

# 2. Set local NLTK data path (if you want to use custom folder)
nltk.data.path.append(os.path.abspath("nltk_data"))

# 3. Download the 'punkt' tokenizer
nltk.download('punkt')


# 4. Define intents for the chatbot
# Intents are the categories of user queries that the chatbot can understand and respond to.
intents = [
    {
        "tag": "greeting",
        "patterns": ["Hi", "Hello", "Hey", "How are you", "What's up"],
        "responses": ["Hi there", "Hello", "Hey", "I'm fine, thank you", "Nothing much"]
    },
    {
        "tag": "goodbye",
        "patterns": ["Bye", "See you later", "Goodbye", "Take care"],
        "responses": ["Goodbye", "See you later", "Take care"]
    },
    {
        "tag": "thanks",
        "patterns": ["Thank you", "Thanks", "Thanks a lot", "I appreciate it"],
        "responses": ["You're welcome", "No problem", "Glad I could help"]
    },
    {
        "tag": "about",
        "patterns": ["What can you do", "Who are you", "What are you", "What is your purpose"],
        "responses": ["I am a chatbot", "My purpose is to assist you", "I can answer questions and provide assistance"]
    },
    {
        "tag": "help",
        "patterns": ["Help", "I need help", "Can you help me", "What should I do"],
        "responses": ["Sure, what do you need help with?", "I'm here to help. What's the problem?", "How can I assist you?"]
    },
    {
        "tag": "age",
        "patterns": ["How old are you", "What's your age"],
        "responses": ["I don't have an age. I'm a chatbot.", "I was just born in the digital world.", "Age is just a number for me."]
    },
    {
        "tag": "weather",
        "patterns": ["What's the weather like", "How's the weather today"],
        "responses": ["I'm sorry, I cannot provide real-time weather information.", "You can check the weather on a weather app or website."]
    },
    {
        "tag": "budget",
        "patterns": ["How can I make a budget", "What's a good budgeting strategy", "How do I create a budget"],
        "responses": ["To make a budget, start by tracking your income and expenses. Then, allocate your income towards essential expenses like rent, food, and bills. Next, allocate some of your income towards savings and debt repayment. Finally, allocate the remainder of your income towards discretionary expenses like entertainment and hobbies.", "A good budgeting strategy is to use the 50/30/20 rule. This means allocating 50% of your income towards essential expenses, 30% towards discretionary expenses, and 20% towards savings and debt repayment.", "To create a budget, start by setting financial goals for yourself. Then, track your income and expenses for a few months to get a sense of where your money is going. Next, create a budget by allocating your income towards essential expenses, savings and debt repayment, and discretionary expenses."]
    },
    {
        "tag": "credit_score",
        "patterns": ["What is a credit score", "How do I check my credit score", "How can I improve my credit score"],
        "responses": ["A credit score is a number that represents your creditworthiness. It is based on your credit history and is used by lenders to determine whether or not to lend you money. The higher your credit score, the more likely you are to be approved for credit.", "You can check your credit score for free on several websites such as Credit Karma and Credit Sesame."]
    }
]


# 5. Create the Vectorizer and Logistic Regression model
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000000)

# 6. Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent ['patterns']:
        tags.append (intent['tag'])
        patterns.append(pattern)

# 7. Training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit (x,y)

#8. Use python to write the chatbot 
def chatbot(input_text):
    input_text =  vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response
        

#9. Deploy the chatbot using UI features of streamlit library

counter = 0

def main():

    try:
        global counter 
        st.title("Sam's Chatbot")
        st.write ("Welcome to the chatbot. Please Type a message and press Enter to start conversation")

        counter += 1
        user_input  = st.text_input("You :", key = f"user_input_{counter}")

        if user_input:
            response = chatbot(user_input)
            st.text_area("Chtbot :", value =  response, height =100, max_chars = None , key = f"chatbot_response_{counter}")

            if response.lower() in ['goodbye','bye']:
                st.write("Thank you for chatting with me. Have a great day!")
                st.stop()
    except Exception as e:
        print ("The program stopped due to the following ERROR :  ",e )


if __name__ == '__main__':
    main()

