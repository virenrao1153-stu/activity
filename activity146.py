import tkinter as tk
from datetime import date

root = tk.Tk()
root.geometry("400x400")
root.title("Age Calculator App")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame, text="Date").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame, text="Month").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame, text="Year").grid(row=3, column=0, padx=10, pady=5, sticky="e")

name_entry = tk.Entry(frame)
date_entry = tk.Entry(frame)
month_entry = tk.Entry(frame)
year_entry = tk.Entry(frame)

name_entry.grid(row=0, column=1, pady=5)
date_entry.grid(row=1, column=1, pady=5)
month_entry.grid(row=2, column=1, pady=5)
year_entry.grid(row=3, column=1, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=20)

def calculate_age():
    name = name_entry.get()
    d = int(date_entry.get())
    m = int(month_entry.get())
    y = int(year_entry.get())
    today = date.today()
    age = today.year - y - ((today.month, today.day) < (m, d))
    result_label.config(text=f"Hello {name}, your present age is {age} years")

tk.Button(root, text="Calculate Age", command=calculate_age).pack()

root.mainloop()