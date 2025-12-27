from tkinter import *

root = Tk()
root.title('Number Pad')
root.geometry('250x300')

nums = [[9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
        ['#', 0, '*']]

# Configure grid
for i in range(4):
    root.rowconfigure(i, weight=1, minsize=50)

for j in range(3):
    root.columnconfigure(j, weight=1, minsize=75)

# Create keypad
for i in range(4):
    for j in range(3):
        frame = Frame(root, relief=SUNKEN, borderwidth=1)
        frame.grid(row=i, column=j, sticky="nsew")

        label = Label(
            frame,
            text=nums[i][j],
            bg='#d0efff',
            font=('Arial', 14)
        )
        label.pack(expand=True, fill="both", padx=3, pady=3)

root.mainloop()