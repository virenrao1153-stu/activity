from tkinter import *
import math

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

def calculate():
    p = float(principal_entry.get())
    t = float(time_entry.get())
    r = float(rate_entry.get())

    si = (p * t * r) / 100
    ci = p * (math.pow((1 + r / 100), t)) - p

    si_value.config(text=f"Simple Interest: {si:.2f}")
    ci_value.config(text=f"Compound Interest: {ci:.2f}")

Label(root, text="Principal").grid(row=0, column=0, padx=10, pady=10)
Label(root, text="Time (years)").grid(row=1, column=0, padx=10, pady=10)
Label(root, text="Rate (%)").grid(row=2, column=0, padx=10, pady=10)

principal_entry = Entry(root)
time_entry = Entry(root)
rate_entry = Entry(root)

principal_entry.grid(row=0, column=1)
time_entry.grid(row=1, column=1)
rate_entry.grid(row=2, column=1)

Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=15)

si_value = Label(root, text="Simple Interest: ")
ci_value = Label(root, text="Compound Interest: ")

si_value.grid(row=4, column=0, columnspan=2)
ci_value.grid(row=5, column=0, columnspan=2)

root.mainloop()