print("Hello! I am your chatbot 🤖")

name = input("What is your name? ")
print("Nice to meet you,", name)

while True:
    mood = input("How are you feeling today? (happy/sad/angry/okay): ").lower()

    if mood == "happy":
        print("That's great! Keep smiling 😊")
    elif mood == "sad":
        print("I'm sorry to hear that. I hope things get better 💙")
    elif mood == "angry":
        print("Take a deep breath. Everything will be okay 😌")
    elif mood == "okay":
        print("Alright! Hope your day goes well 🙂")
    else:
        print("I didn't understand that mood.")

    choice = input("Do you want to continue chatting? (yes/no): ").lower()

    if choice == "no":
        print("Goodbye,", name, "! Have a nice day 👋")
        break