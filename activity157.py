from tkinter import *

root = Tk()
root.title("Length Converter App")
root.geometry("400x400")

def check_strength():
    length = len(password_entry.get())

    if length <= 5:
        result.config(text="Weak", fg="red")
    elif 6 <= length <= 8:
        result.config(text="Medium", fg="yellow")
    elif 9 <= length <= 12:
        result.config(text="Strong", fg="light green")
    else:
        result.config(text="Very Strong", fg="dark green")

Label(root, text="Enter Password").pack(pady=20)

password_entry = Entry(root, show="*")
password_entry.pack(pady=10)

Button(root, text="Check Strength", command=check_strength).pack(pady=15)

result = Label(root, text="", font=("Arial", 14))
result.pack(pady=20)

root.mainloop()