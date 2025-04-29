import tkinter as tk
import random

def generate_password():
    label["text"] = "".join(random.choices("abc123", k=6))

window = tk.Tk()
window.title("main window")
window.geometry("300x300")

button = tk.Button(window, text="press here to generate a password", command=generate_password)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()
