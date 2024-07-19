import random

def chatbot_response(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey!"],
        "how are you": ["I'm good, thanks!", "Doing well, how about you?", "I'm just a bot, but I'm functioning properly!"],
        "what's your name": ["I'm a chatbot created by OpenAI.", "You can call me ChatGPT.", "I am a nameless bot, but you can give me one!"],
        "bye": ["Goodbye!", "See you later!", "Take care!"]
    }
    
    user_input = user_input.lower()
    
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return "I'm not sure how to respond to that."

def chat():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
