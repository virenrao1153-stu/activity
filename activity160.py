from textblob import TextBlob
from colorama import Fore, Style, init

init()

print(Fore.CYAN + "🤖 Welcome to Sentiment Spy Chatbot!" + Style.RESET_ALL)

name = input("Enter your name: ")
print("Hello,", name)

conversation_history = []
positive_count = 0
negative_count = 0
neutral_count = 0

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print(Fore.YELLOW + "Chat ended. Goodbye!" + Style.RESET_ALL)
        break

    conversation_history.append(user_input)

    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
        positive_count += 1
        print(Fore.GREEN + "Bot: That sounds positive!" + Style.RESET_ALL)
    elif polarity < 0:
        sentiment = "Negative 😟"
        negative_count += 1
        print(Fore.RED + "Bot: That sounds a bit negative." + Style.RESET_ALL)
    else:
        sentiment = "Neutral 😐"
        neutral_count += 1
        print(Fore.BLUE + "Bot: That sounds neutral." + Style.RESET_ALL)

    print("Detected Sentiment:", sentiment)

    choice = input("\nDo you want to continue? (yes/no): ").lower()
    if choice == "no":
        break

print("\n📊 Sentiment Summary:")
print("Positive messages:", positive_count)
print("Negative messages:", negative_count)
print("Neutral messages:", neutral_count)
print("Thank you for using Sentiment Spy!")