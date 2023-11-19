import tkinter as tk
import re  # for making password checking simpler
from User import UserClass
from Dashboard import DashboardClass



    
        
class LoginPageClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Login Page", font = ('Times New Roman',20, "bold"))
        self.controller = controller
        label.pack(pady=20)

        back_button = tk.Button(
            self,
            text="Back",
            command=lambda: self.controller.show_welcome()
        )
        back_button.pack(side="top", anchor="nw")

        entry_frame = tk.Frame(self)
        username_label = tk.Label(entry_frame, text="Username:")
        password_label = tk.Label(entry_frame, text="Password:")
        self.username_entry = tk.Entry(entry_frame)
        self.password_entry = tk.Entry(entry_frame)
        message_box = tk.Label(entry_frame, text="Please enter your username and password")
        login_button = tk.Button(entry_frame, text="Login",
                                 command = lambda: self.attempt_login(self.username_entry.get(), 
                                                                      self.password_entry.get(),
                                                                      message_box))

        username_label.grid(column=0,row=0)
        password_label.grid(column=0,row=1)
        self.username_entry.grid(column=1,row=0,columnspan=2)
        self.password_entry.grid(column=1,row=1,columnspan=2)
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
        # delete text from boxes
        potential_user.serial_exists = False
        self.password_entry.delete(0,len(self.password_entry.get()))
        self.username_entry.delete(0,len(self.username_entry.get()))  
        self.controller.load_dashboard(potential_user)
        self.controller.set_egram_user(potential_user)
        
        self.controller.show_frame(DashboardClass)

        

    




        

