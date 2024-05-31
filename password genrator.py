"""password"""

import random
import string
import tkinter as tk
from tkinter import Label, Entry, Button

def generate_password(length):
    digits = string.digits
    password = random.choice(digits)
    remaining_characters = string.ascii_letters + string.digits + string.punctuation
    password += ''.join(random.choice(remaining_characters) for _ in range(length - 1))
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

def generate_password_and_update_label():
    label_result.config(text="")  # Clear the label text
    try:
        password_length = int(entry_length.get())
        generated_password = generate_password(password_length)
        label_result.config(text=f"Generated Password: {generated_password}")
    except ValueError:
        label_result.config(text="Please enter a valid integer for the password length.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create and place GUI elements
Label(window, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
entry_length = Entry(window)
entry_length.grid(row=0, column=1, padx=10, pady=10)

button_generate = Button(window, text="Generate Password", command=generate_password_and_update_label)
button_generate.grid(row=1, column=0, columnspan=2, pady=10)

label_result = Label(window, text="")
label_result.grid(row=2, column=0, columnspan=2, pady=10)
label_result.config(wraplength=150)

# Run the GUI
window.mainloop()
