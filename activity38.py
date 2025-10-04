import random
import pyttsx3
import time

# Initialize Text-to-Speech
engine = pyttsx3.init()
engine.setProperty('rate', 165)
engine.setProperty('volume', 1.0)

def speak(text):
    """Speaks the text aloud"""
    print("😂 Anime JokeBot:", text)
    engine.say(text)
    engine.runAndWait()

# Naruto jokes 🌀
naruto_jokes = [
    "Why did Naruto bring ramen to class? Because he wanted to be the top noodle of his village!",
    "Why did Sasuke open a bakery? Because he wanted to make everyone feel his buns of revenge!",
    "Why was Sakura always calm? Because she had perfect chakra control… over her anger!",
    "How does Kakashi read so many books? With sharingan speed reading mode!",
    "Why did Itachi cross the road? To say ‘Sorry, Sasuke’ one more time!",
    "Why did Gaara never lose at cards? Because the sand always had his back!",
    "Why doesn’t Naruto ever get cold? Because he always wears the Nine-Tail coat!"
]

# Demon Slayer jokes 🗡️
demonslayer_jokes = [
    "Why did Tanjiro become a great musician? Because he always finds the right note breathing!",
    "Why did Inosuke join a gym? Because the mountain just wasn’t enough for those abs!",
    "Why did Zenitsu carry a pillow everywhere? In case thunder struck him while napping!",
    "Why did Nezuko refuse to fight? Because she didn’t want to lose her cool… or her bamboo!",
    "Why did Muzan start a skincare brand? Because he really knows how to stay young forever!",
    "Why did Rengoku love barbecues? Because he’s always fired up!",
    "Why did Giyu get kicked out of the party? Because he’s always so water-breathing serious!"
]

def get_joke():
    """Returns a random joke from either Naruto or Demon Slayer"""
    all_jokes = naruto_jokes + demonslayer_jokes
    return random.choice(all_jokes)

def main():
    speak("Welcome to Anime JokeBot! I’ve got jokes from Naruto and Demon Slayer!")
    while True:
        choice = input("\nPress ENTER for a new anime joke or type 'q' to quit: ").lower().strip()
        if choice == 'q':
            speak("Alright! Stay awesome like a Hashira or a Hokage! Goodbye!")
            break
        joke = get_joke()
        speak(joke)
        time.sleep(1)

if __name__ == "__main__":
    main()
