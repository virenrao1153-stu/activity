from tkinter import *
import random

root = Tk()
root.title("Length Converter App")
root.geometry("400x400")

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)

    user_label.config(text="Your Choice: " + user_choice)
    computer_label.config(text="Computer Choice: " + computer_choice)

    if user_choice == computer_choice:
        result_label.config(text="Result: Draw")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="Result: You Win")
    else:
        result_label.config(text="Result: Computer Wins")

Label(root, text="Rock Paper Scissors", font=("Arial", 16)).pack(pady=20)

Button(root, text="Rock", width=10, command=lambda: play("Rock")).pack(pady=5)
Button(root, text="Paper", width=10, command=lambda: play("Paper")).pack(pady=5)
Button(root, text="Scissors", width=10, command=lambda: play("Scissors")).pack(pady=5)

user_label = Label(root, text="")
user_label.pack(pady=10)

computer_label = Label(root, text="")
computer_label.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()