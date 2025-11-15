import random

secret = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20.")

while True:
    guess = int(input("Your guess: "))

    if guess == secret:
        print("Correct! You guessed it!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")