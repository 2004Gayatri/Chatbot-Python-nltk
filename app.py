from flask import Flask, request, jsonify
import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize Flask app
app = Flask(__name__)

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Define intents
intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening", "what's up"],
        "responses": ["Hello! How can I help you today?", "Hi there! What's on your mind?", "Hey! How's it going?"]
    },
    "farewell": {
        "patterns": ["bye", "goodbye", "see you", "take care"],
        "responses": ["Goodbye! Have a great day!", "See you later!", "Take care!"]
    },
    "default": {
        "patterns": [],
        "responses": ["I'm sorry, I don't understand. Could you rephrase that?"]
    }
}

# Function to preprocess and lemmatize input
def preprocess(text):
    tokens = word_tokenize(text.lower())
    return [lemmatizer.lemmatize(token) for token in tokens]

# Function to get intent based on user input
def get_intent(user_input):
    lemmatized_input = preprocess(user_input)
    for intent, intent_data in intents.items():
        for pattern in intent_data["patterns"]:
            if pattern in ' '.join(lemmatized_input):
                return intent
    return "default"

# Root route for testing
@app.route('/')
def home():
    return "Server is running!"

# Chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()  # Get JSON data from the request
        if not data or 'message' not in data:
            return jsonify({"error": "Invalid request. Please provide a 'message' field."}), 400

        user_message = data['message']  # Extract user message
        intent = get_intent(user_message)  # Get intent
        response = random.choice(intents[intent]["responses"])  # Get response
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
