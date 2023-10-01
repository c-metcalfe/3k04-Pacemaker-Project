import tkinter as tk

def attempt_login():
    print("login?")
        
class LoginPageClass(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Login Page")
        label.pack(padx=10, pady=10)

        back_button = tk.Button(
            self,
            text="Back",
            command=lambda: self.lower()
        )
        back_button.pack(side="top", anchor="nw")

        entry_frame = tk.Frame(self)
        username_label = tk.Label(entry_frame, text="Username:")
        password_label = tk.Label(entry_frame, text="Password:")
        username_entry = tk.Entry(entry_frame)
        password_entry = tk.Entry(entry_frame)
        login_button = tk.Button(entry_frame, text="Login",
                                 command = lambda: attempt_login())

        username_label.grid(column=0,row=0)
        password_label.grid(column=0,row=1)
        username_entry.grid(column=1,row=0,columnspan=2)
        password_entry.grid(column=1,row=1,columnspan=2)
        login_button.grid(row=2,column=1)

        entry_frame.pack(side="top")

    




        
