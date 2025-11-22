import random

print("Welcome to the Python Practice Quiz!")
print("------------------------------------")
print("This quiz uses basic concepts + the random module.\n")

score = 0

print("Q1: Guess the number (between 1 and 5)")
secret = random.randint(1, 5)
guess = int(input("Enter your guess: "))

if guess == secret:
    print("Correct! 🎉")
    score += 1
else:
    print(f"Wrong! The correct number was {secret}.")

print()

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

print(f"Q2: What is {num1} + {num2}?")
answer = int(input("Your answer: "))

if answer == num1 + num2:
    print("Correct! 👍")
    score += 1
else:
    print(f"Incorrect! The right answer is {num1 + num2}.")

print()

words = ["apple", "banana", "mango", "grapes"]
choice = random.choice(words)

print("Q3: A random fruit has been selected.")
user = input("Type any fruit name and see if it matches: ")

if user.lower() == choice:
    print("Wow! You matched it! ⭐")
    score += 1
else:
    print(f"Not matched! The selected fruit was: {choice}")

print()

print("------------------------------------")
print(f"Your total score: {score} / 3")
print("Thank you for practising Python with random module!")