import tkinter as tk
import re  # for making password checking simpler
from User import UserClass
from Dashboard import DashboardClass


    
        
class LoginPageClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Login Page")
        self.controller = controller
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
        message_box = tk.Label(entry_frame, text="Please enter your username and password")
        login_button = tk.Button(entry_frame, text="Login",
                                 command = lambda: self.attempt_login(username_entry.get(), 
                                                                      password_entry.get(),
                                                                      message_box))

        username_label.grid(column=0,row=0)
        password_label.grid(column=0,row=1)
        username_entry.grid(column=1,row=0,columnspan=2)
        password_entry.grid(column=1,row=1,columnspan=2)
        login_button.grid(row=2,column=1)
        message_box.grid(row=3, column=0,columnspan=3)

        entry_frame.pack(side="top")

    def attempt_login(self, username, password, message_box):
        message_box.config(text="")
        
        potential_user = UserClass(username)
        if not potential_user.file_found:
            message_box.config(text="Error: Username not found.")
            return
        
        if (password != potential_user.password):
            message_box.config(text="Error: Incorrect Password.")
            return
        
        self.controller.load_dashboard(potential_user)
        self.controller.show_frame(DashboardClass)

        

    




        
