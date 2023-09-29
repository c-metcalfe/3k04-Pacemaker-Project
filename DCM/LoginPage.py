import tkinter as tk

class LoginPageClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Login Page")
        label.pack(padx=10, pady=10)

        
