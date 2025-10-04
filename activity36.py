import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen from microphone and return recognized text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak your calculation (e.g., '12 plus 4 times 2'):")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand.")
    except sr.RequestError:
        speak("Speech service unavailable.")
    return None

def evaluate_expression(expr):
    """Evaluate math expression safely"""
    try:
        # Replace words with symbols
        expr = expr.replace("plus", "+").replace("minus", "-")
        expr = expr.replace("times", "*").replace("multiplied by", "*")
        expr = expr.replace("divided by", "/").replace("over", "/")
        expr = expr.replace("into", "*").replace("x", "*")
        expr = expr.replace("power", "**").replace("^", "**")

        result = eval(expr)
        return result
    except Exception:
        return None

def main():
    speak("Hello! I am your voice calculator.")
    while True:
        choice = input("\nType 'v' for voice input, 't' to type, or 'q' to quit: ").lower()

        if choice == 'q':
            speak("Goodbye!")
            break
        elif choice == 'v':
            query = listen()
        elif choice == 't':
            query = input("Enter your calculation: ").lower()
        else:
            print("Invalid choice.")
            continue

        if not query:
            continue

        result = evaluate_expression(query)
        if result is not None:
            speak(f"The answer is {result}")
        else:
            speak("Sorry, I couldn’t calculate that.")

if __name__ == "__main__":
    main()
