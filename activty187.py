import requests

def get_random_jokes():
    """Fetch a random joke from the official Joke API."""
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        
        print(f"Full JSON Response: {response.json()}")

        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "Failed to retrieve joke."
    
def main():
    print("Welcome to the Random Joke Generator!")

    while True:
        user_input = input("Press Enter to get a random joke or type 'exit' to quit: ").strip().lower()

        if user_input in ("q", "exit"):
            print("Goodbye!")
            break

        joke = get_random_jokes()
        print(f"Here's your joke: {joke}\n")

if __name__ == "__main__"
    main()