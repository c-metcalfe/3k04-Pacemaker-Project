import tkinter as tk
from RegisterPage import RegisterPageClass
from LoginPage import LoginPageClass

class WelcomePageClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "WELCOME", font= ('Times New Roman',60, "bold"))
        label.pack(padx = 200, pady = 130)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function

        login_button = tk.Button(
            self,
            text="Login",
            font = 18,
            width = 10,
            height = 2,
            command=lambda: controller.show_frame(LoginPageClass),
        )
        login_button.pack(anchor="center", pady="20")

        register_button = tk.Button(
            self,
            text="Register new user", 
            font = 18,
            width = 25,
            height = 2,
            command=lambda: controller.show_frame(RegisterPageClass),
        )
        register_button.pack() 





