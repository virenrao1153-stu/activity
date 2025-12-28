from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Getting Started with Widgets")

title_label = Label(root, text="This application multiplies two numbers", fg="blue")
title_label.pack(pady=5)

label1 = Label(root, text="Enter first number")
label1.pack()

entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text="Enter second number")
label2.pack()

entry2 = Entry(root)
entry2.pack()

result_box = Text(root, height=2, width=25)
result_box.pack(pady=5)

def calculate():
    result_box.delete("1.0", END)
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_box.insert(END, num1 * num2)
    except:
        result_box.insert(END, "Invalid Input")

button = Button(root, text="Calculate Product", command=calculate, bg="green", fg="white")
button.pack(pady=5)

root.mainloop()