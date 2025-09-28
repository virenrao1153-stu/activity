import requests

def get_meaning(word: str):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    data = resp.json()
    # It returns a list of entries; pick the first meaning
    try:
        meanings = data[0]["meanings"]
        # get first definition under the first meaning
        first_def = meanings[0]["definitions"][0]["definition"]
        return first_def
    except Exception as e:
        return None

def main():
    word = input("Enter a word: ").strip().lower()
    meaning = get_meaning(word)
    if meaning:
        print(f"{word} = {meaning}")
    else:
        print("Not a word, try again!!!")

if __name__ == "__main__":
    main()
