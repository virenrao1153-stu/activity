import requests

API_URL = "https://uselessfacts.jsph.pl/random.json?language=en"
FILE_NAME = "facts.txt"


def get_fact():
    try:
        response = requests.get(API_URL)
        data = response.json()
        return data['text']
    except:
        return "Error fetching fact."
    


    def save_fact(fact):
        file = open(FILE_NAME, "a")
        file.write(fact + "\n")
        file.close()
        print("Fact saved successfully!\n")



def show_fact():
    try:
        file = open(FILE_NAME, "r")
        facts = file.readlines()

        if len(facts) == 0:
            print("No facts saved yet.\n")
        else:
            print("\nSaved Facts:")
            for i, fact in enumerate(facts, 1):
                print(i, "-", fact.strip())
        file.close()

    except FileNotFoundError:
        print("No facts saved yet.\n")



while True:

    print("\n===== FACTS API PROGRAM =====")
    print("1. Get a random fact")
    print("2. Get multiple facts")
    print("3. Show saved facts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        fact = get_fact()
        print("\nFact:", fact)

        save = input("Do you want to save this fact? (y/n): ")
        if save.lower() == "y":
            save_fact(fact)

    elif choice == "2":
        n = int(input("How many facts do you want to get? "))
        for i in range(n):
            fact = get_fact()
            print(f"\nFact {i + 1}: {fact}")

    elif choice == "3":
        show_facts()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")