import customtkinter
import pyperclip
import random
import string

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

class CheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.char_label = customtkinter.CTkLabel(
            self, text="Password lenght: 15", width=40, 
            font=customtkinter.CTkFont(size=15, weight="bold"))
        self.char_label.grid(row=0, column=0, padx=20, pady=20)

        self.slider = customtkinter.CTkSlider(
            self, from_=1, to=30, command=self.update_char_label)
        self.slider.grid(row=1, column=0, padx=20, pady=20)

        self.checkbox_1 = customtkinter.CTkCheckBox(
            self, text="Include Uppercase Letters", 
            font=customtkinter.CTkFont(size=15, weight="bold"))
        self.checkbox_1.grid(row=2, column=0, padx=20, pady=20, sticky="w")

        self.checkbox_2 = customtkinter.CTkCheckBox(
            self, text="Include Lowercase Letters", 
            font=customtkinter.CTkFont(size=15, weight="bold"))
        self.checkbox_2.grid(row=3, column=0, padx=20, pady=20, sticky="w")

        self.checkbox_3 = customtkinter.CTkCheckBox(
            self, text="Include Numbers", 
            font=customtkinter.CTkFont(size=15, weight="bold"))
        self.checkbox_3.grid(row=4, column=0, padx=20, pady=20, sticky="w")

        self.checkbox_4 = customtkinter.CTkCheckBox(
            self, text="Include Symbols", 
            font=customtkinter.CTkFont(size=15, weight="bold"))
        self.checkbox_4.grid(row=5, column=0, padx=20, pady=20, sticky="w")

    def update_char_label(self, value):
        value = self.slider.get()
        rounded_value = int(value)
        self.char_label.configure(text=f"Password lenght: {rounded_value}")

class PasswordFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = customtkinter.CTkLabel(self, text="Press Generate to ", 
            fg_color="transparent", width=300, 
            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label.grid(row=7, column=0, padx=10, pady=10)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator")
        self.geometry("400x600")
        self.grid_columnconfigure(0, weight=1)

        self.checkbox_frame = CheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=10)

        self.password_frame = PasswordFrame(self)
        self.password_frame.grid(row=7, column=0, padx=10, pady=10)

        self.button = customtkinter.CTkButton(self, text="Generate", 
            command=self.generate_password, 
            font=customtkinter.CTkFont(size=12, weight="bold"))
        self.button.grid(row=6, column=0, padx=10, pady=10)

        self.button1 = customtkinter.CTkButton(self, text="Copy Password", 
            command=self.copy_password, 
            font=customtkinter.CTkFont(size=12, weight="bold"))
        self.button1.grid(row=8, column=0, padx=10, pady=10)

        self.checkbox_frame.checkbox_1.select()
        self.checkbox_frame.checkbox_2.select()
        self.checkbox_frame.checkbox_3.select()
        self.checkbox_frame.checkbox_4.select()

        self.generate_password()

    def generate_password(self):
        try:
            inUppercase = False
            inLowercase = False
            inNumbers = False
            inSymbols = False

            if not any([inUppercase, inLowercase, inNumbers, inSymbols]):
                self.password_frame.label.configure(
                    text="Please select at least 1 checkbox")

            if self.checkbox_frame.checkbox_1.get() == 1:
                inUppercase = True
            if self.checkbox_frame.checkbox_2.get() == 1:
                inLowercase = True
            if self.checkbox_frame.checkbox_3.get() == 1:
                inNumbers = True
            if self.checkbox_frame.checkbox_4.get() == 1:
                inSymbols = True

            pass_chars = []
            if inUppercase:
                pass_chars += string.ascii_uppercase
            if inLowercase:
                pass_chars += string.ascii_lowercase
            if inNumbers:
                pass_chars += string.digits
            if inSymbols:
                pass_chars += string.punctuation

            pass_length = self.checkbox_frame.slider.get()
            self.password = ''.join(random.choice(pass_chars) 
                for _ in range(int(pass_length)))
            self.password_frame.label.configure(text=self.password)
            
        except Exception as e:
            print(f"An error occurred: {e}")

    def copy_password(self):
        pyperclip.copy(self.password)
        self.button1.configure(text="Password Copied!")
        self.after(2000, lambda: self.button1.configure(text="Copy Password"))

if __name__ == "__main__":
    app = App()
    app.mainloop()