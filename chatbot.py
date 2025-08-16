import sys
import random
from datetime import datetime

def simple_chatbot():
    print("Welcome to the Simple Chatbot! Type 'exit' or 'bye' to quit.")
    
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one wall say to the other? I'll meet you at the corner!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What do you call a bear with no teeth? A gummy bear!"
    ]
    
    facts = [
        "Did you know? Honey never spoils. Archaeologists have discovered pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "Octopuses have three hearts: two pump blood through the gills, while the third pumps it through the rest of the body.",
        "A flock of crows is known as a murder.",
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
        "Bananas are berries, but strawberries aren't.",
        "A group of flamingos is called a 'flamboyance'.",
        "The unicorn is the national animal of Scotland."
    ]
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm doing great, thanks for asking! How about you?")
        elif "name" in user_input:
            print("Chatbot: My name is SimpleBot, built by Grok.")
        elif "weather" in user_input:
            print("Chatbot: I'm sorry, I don't have real-time weather data, but it's always sunny in the digital world!")
        elif "time" in user_input:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        elif "date" in user_input:
            current_date = datetime.now().strftime("%Y-%m-%d")
            print(f"Chatbot: Today's date is {current_date}.")
        elif "day" in user_input:
            current_day = datetime.now().strftime("%A")
            print(f"Chatbot: Today is {current_day}.")
        elif "joke" in user_input or "funny" in user_input:
            print(f"Chatbot: {random.choice(jokes)}")
        elif "fact" in user_input or "interesting" in user_input:
            print(f"Chatbot: {random.choice(facts)}")
        elif "favorite color" in user_input:
            print("Chatbot: My favorite color is electric blue – it really sparks joy!")
        elif "hobby" in user_input or "hobbies" in user_input:
            print("Chatbot: I love chatting with humans and learning new things. What's yours?")
        elif "math" in user_input or "calculate" in user_input:
            # Simple example: extract two numbers and add them if "add" is mentioned
            if "add" in user_input:
                try:
                    nums = [int(word) for word in user_input.split() if word.isdigit()]
                    if len(nums) >= 2:
                        result = sum(nums[:2])
                        print(f"Chatbot: The sum is {result}.")
                    else:
                        print("Chatbot: Please provide at least two numbers to add.")
                except:
                    print("Chatbot: Sorry, I couldn't parse the numbers.")
            else:
                print("Chatbot: I'm not great at complex math, but try asking me to 'add' two numbers!")
        elif "what can you do" in user_input or "help" in user_input:
            print("Chatbot: I can do a few things! Here's what I can respond to:\n"
                  "- Greet you (say 'hello' or 'hi')\n"
                  "- Tell you how I'm doing ('how are you')\n"
                  "- Share my name ('what's your name')\n"
                  "- Joke around ('tell me a joke' or 'something funny')\n"
                  "- Share interesting facts ('tell me a fact' or 'something interesting')\n"
                  "- Reveal my favorite color ('favorite color')\n"
                  "- Talk about hobbies ('what are your hobbies')\n"
                  "- Do simple math like adding numbers ('add 5 and 3')\n"
                  "- Tell you the current time ('what time is it')\n"
                  "- Tell you today's date ('what's the date')\n"
                  "- Tell you the day of the week ('what day is it')\n"
                  "- And more – just chat and see!")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a nice day.")
            sys.exit(0)
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you rephrase?")
            
# Run the chatbot
if __name__ == "__main__":
    simple_chatbot()