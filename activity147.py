import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")

frame = tk.Frame(root)
frame.pack(pady=40)

tk.Label(frame, text="Length in meters").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(frame)
entry.grid(row=0, column=1, padx=10, pady=10)

result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=20)

def convert():
    meters = float(entry.get())
    cm = meters * 100
    result.config(text=f"Length in centimeters: {cm}")

tk.Button(root, text="Convert", command=convert).pack()

root.mainloop()