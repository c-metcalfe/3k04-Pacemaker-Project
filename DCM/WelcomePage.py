import tkinter as tk
from RegisterPage import RegisterPageClass
from LoginPage import LoginPageClass

class WelcomePageClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome Page"
                         
                         )
        label.pack(padx=100, pady=100)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        login_button = tk.Button(
            self,
            text="Login",
            command=lambda: controller.show_frame(LoginPageClass),
        )
        login_button.pack(side="bottom", pady="10")

        register_button = tk.Button(
            self,
            text="Register new user",
            command=lambda: controller.show_frame(RegisterPageClass),
        )
        register_button.pack(side="bottom")



