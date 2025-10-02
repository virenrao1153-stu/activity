import cv2
import random

# Animal database
animals = {
    "Lion": "You are brave, confident, and a natural leader.",
    "Dolphin": "You are smart, friendly, and playful.",
    "Owl": "You are wise, calm, and thoughtful.",
    "Dragon": "You are powerful, mysterious, and strong-willed.",
    "Unicorn": "You are unique, magical, and full of imagination.",
    "Shark": "You are strong, determined, and focused.",
    "Wolf": "You are loyal, protective, and a team player.",
    "Phoenix": "You always rise again from challenges with new strength."
}

# User input
name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender (M/F/Other): ")

# Open webcam for face scan
print("\nOpening camera... Look at the screen 👀")
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Once face detected → break loop
        cap.release()
        cv2.destroyAllWindows()
        print("Face detected ✅")
        
        # Random animal match
        animal = random.choice(list(animals.keys()))
        print("\n==============================")
        print(f"Hello {name} 👋")
        print(f"Your spirit animal is: {animal} 🐾")
        print("Description:", animals[animal])
        print("==============================")
        exit()

    cv2.imshow('Face Scanner - Press Q to Quit', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
