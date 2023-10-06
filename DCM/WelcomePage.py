import tkinter as tk
from RegisterPage import RegisterPageClass
from LoginPage import LoginPageClass

class WelcomePageClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "WELCOME", font= ('Times New Roman',50, "bold"))
        label.pack(padx="200", pady="180")

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        login_button = tk.Button(
            self,
            text="Login",
            font = 15,
            command=lambda: controller.show_frame(LoginPageClass),
        )
        login_button.pack(side="bottom", pady="10")

        register_button = tk.Button(
            self,
            text="Register new user", 
            font = 15,
            command=lambda: controller.show_frame(RegisterPageClass),
        )
        register_button.pack(side="bottom")



