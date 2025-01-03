import nltk
import random
import re

nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Define the intents with patterns and responses
intents = {
    "greeting": {
        "patterns": [
            "hello", "hi", "hey", "good morning", "good evening", "what's up", "hiya", 
            "howdy", "greetings", "sup", "yo"
        ],
        "responses": [
            "Hello! How can I help you today?", 
            "Hi there! What's on your mind?", 
            "Hey! How's everything going?", 
            "Howdy! How can I assist you?", 
            "Hiya! What do you need help with?"
        ]
    },
    "farewell": {
        "patterns": [
            "bye", "goodbye", "see you", "take care", "see you later", "catch you later", 
            "farewell", "adios", "ciao", "later", "peace out"
        ],
        "responses": [
            "Goodbye! Have a great day!", 
            "See you later! Take care!", 
            "Bye! Hope to chat again soon.", 
            "Adios! Stay safe!", 
            "Ciao! Talk to you next time."
        ]
    },
    "how_are_you": {
        "patterns": [
            "how are you", "how's it going", "how are you doing", "what's up with you", 
            "are you okay", "how do you feel", "how's everything", "how are things"
        ],
        "responses": [
            "I'm just a bot, but I'm doing great! How about you?", 
            "I'm here and ready to chat! How are you?", 
            "I don't have feelings, but I'm here to help you. How are you?"
        ]
    },
    "feeling_response": {
        "patterns": [
            "i am fine", "i am good", "i am ok", "i am doing well", "i'm fine", 
            "i'm good", "i'm ok", "doing well", "i'm alright", "feeling good"
        ],
        "responses": [
            "That's great to hear! How can I assist you?", 
            "Awesome! Let me know if you need any help.", 
            "Glad to hear you're doing well. What can I do for you?", 
            "Good to know! How can I make your day better?"
        ]
    },
    "thanks": {
        "patterns": [
            "thank you", "thanks", "thanks a lot", "thank you so much", "I appreciate it", 
            "many thanks", "thanks a bunch", "thanks a ton", "grateful", "thank you kindly"
        ],
        "responses": [
            "You're welcome!", 
            "No problem at all!", 
            "Happy to help!", 
            "Always here to assist you!", 
            "You're most welcome!"
        ]
    },
    "default": {
        "patterns": [],  # Empty patterns for the default response
        "responses": [
            "I'm sorry, I don't understand. Can you rephrase that?", 
            "Hmm, I don't have an answer for that.", 
            "That's interesting! Tell me more.", 
            "Sorry, I didn't get that. Could you explain it differently?"
        ]
    }
}

# Preprocess and lemmatize input
def preprocess(text):
    tokens = word_tokenize(text.lower())  # Tokenize input
    return [lemmatizer.lemmatize(token) for token in tokens]  # Lemmatize

# Function to get intent based on user input
def get_intent(user_input):
    lemmatized_input = preprocess(user_input)  # Preprocess the input
    
    # Loop through intents and patterns
    for intent, intent_data in intents.items():
        for pattern in intent_data["patterns"]:
            # Check if the pattern is a substring of the lemmatized input
            if any(pat in ' '.join(lemmatized_input) for pat in pattern.split()):
                return intent
    
    # Return default intent if no match found
    return "default"

# Chatbot conversation loop
def chatbot():
    print("Chatbot: Hello! I am your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Check for 'bye' to exit
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get intent based on user input
        intent = get_intent(user_input)  
        
        # Get a random response from the matched intent, fallback to default
        response = random.choice(intents.get(intent, intents["default"])["responses"])  
        
        print(f"Chatbot: {response}")

# Start the chatbot
chatbot()
