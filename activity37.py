import pyjokes
import pyttsx3
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)   # speaking speed
engine.setProperty('volume', 1.0) # volume

def speak(text):
    """Speaks the given text aloud"""
    print("🤖 JokeBot:", text)
    engine.say(text)
    engine.runAndWait()

def tell_joke():
    """Fetches and speaks a random joke"""
    joke = pyjokes.get_joke(language="en", category="all")
    speak(joke)

def main():
    speak("Hi! I’m your JokeBot! Ready to laugh?")
    while True:
        choice = input("\nPress ENTER for a new joke or type 'q' to quit: ").lower().strip()
        if choice == 'q':
            speak("Okay, see you later! Stay happy!")
            break
        tell_joke()
        time.sleep(1)

if __name__ == "__main__":
    main()
