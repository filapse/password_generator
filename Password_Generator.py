import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    password_length_str = length_entry.get()
    
    if password_length_str.isdigit() and 1 <=int(password_length_str) <= 50:
        password_length = int(password_length_str)
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for _ in range(password_length))

        # Copy the password to the clipboard
        pyperclip.copy(password)

        result_label.config(text="Generated Password (copied to clipboard): \n" + password)

    else:
        result_label.config(text="Invalid input. Please enter a valid password length.")

def on_enter(event):
    generate_password()

def close_app(event):
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position to center the window
x = (screen_width - 400) // 2  # 400 is the width of the window
y = (screen_height - 200) // 2  # 200 is the height of the window

# Set the window position and size
root.geometry(f"400x200+{x}+{y}")

# Create and pack widgets
length_label = tk.Label(root, text="Password Length (Between 1 and 50 characters):")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Bind the Enter key to the Generate Password function
length_entry.bind("<Return>", on_enter)

# Bind the Escape key to close the app
root.bind("<Escape>", close_app)

# Start the GUI main loop
root.mainloop()