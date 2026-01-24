import re
from colorama import Fore, Style, init

init()

memory_file = "chat_memory.txt"

def save_to_memory(text):
    with open(memory_file, "a") as file:
        file.write(text + "\n")

def load_memory():
    try:
        with open(memory_file, "r") as file:
            return file.readlines()
    except:
        return []

def chatbot_response(user_input):
    user_input = user_input.lower()

    if re.search(r"\bhello\b|\bhi\b|\bhey\b", user_input):
        return Fore.GREEN + "Hello! How can I help you today?" + Style.RESET_ALL

    elif re.search(r"how are you", user_input):
        return Fore.CYAN + "I'm doing great! Thanks for asking 😊" + Style.RESET_ALL

    elif re.search(r"weather", user_input):
        return Fore.YELLOW + "The weather seems pleasant today ☀️ (simulated response)" + Style.RESET_ALL

    elif re.search(r"time", user_input):
        return Fore.MAGENTA + "I can't check real time yet, but I hope it's a good one!" + Style.RESET_ALL

    elif re.search(r"news", user_input):
        return Fore.BLUE + "Here’s a news update: Stay positive and keep learning! 📰" + Style.RESET_ALL

    elif re.search(r"your name", user_input):
        return Fore.CYAN + "I am an Enhanced Rule-Based Chatbot 🤖" + Style.RESET_ALL

    elif re.search(r"bye|exit|quit", user_input):
        return "exit"

    else:
        return Fore.RED + "Sorry, I didn't understand that. Try asking something else." + Style.RESET_ALL


print(Fore.CYAN + "🤖 Enhanced Chatbot Started!" + Style.RESET_ALL)
name = input("Enter your name: ")
print("Welcome,", name)

previous_chats = load_memory()
if previous_chats:
    print(Fore.YELLOW + "\nPrevious Conversation:" + Style.RESET_ALL)
    for line in previous_chats[-3:]:
        print(line.strip())

while True:
    user_text = input("\nYou: ")
    save_to_memory("You: " + user_text)

    response = chatbot_response(user_text)

    if response == "exit":
        print(Fore.GREEN + "Bot: Goodbye! Have a great day 👋" + Style.RESET_ALL)
        break

    print("Bot:", response)
    save_to_memory("Bot: " + response)