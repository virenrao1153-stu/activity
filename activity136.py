from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("200x150")

def handle_keypress(event):
    """Print the character associated with the key pressed"""
    print(event.char)

def handle_click(event):
    print("The button was clicked!")

# Bind key press event to window
window.bind("<Key>", handle_keypress)

# Create button
button = Button(window, text="Click me!")
button.pack(pady=20)

# Bind mouse click event to button
button.bind("<Button-1>", handle_click)

window.mainloop()