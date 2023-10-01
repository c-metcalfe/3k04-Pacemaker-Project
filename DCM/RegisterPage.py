import tkinter as tk
import os

CONST_Max_user_count = 10

def attempt_register():
    print("register?")
    # if not too many users make a new user file in the Users folder, add appropriate info, set all parameters to default values
    users_count = 0
    users_folder_path = "Users"
    for path in os.listdir(users_folder_path):  # count number of existing user files in the user folder
        if os.path.isfile(os.path.join(users_folder_path, path)): # check if current path is a file or folder
            users_count += 1
    
    if users_count >= CONST_Max_user_count:   
        print("Error: Maximum of 10 Users already created")
        return False
    
    # make new user file with a bunch of data in it
    

    




class RegisterPageClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Register Page")
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
        register_button = tk.Button(entry_frame, text="Register new User",
                                 command=lambda: attempt_register())

        username_label.grid(column=0,row=0)
        password_label.grid(column=0,row=1)
        username_entry.grid(column=1,row=0,columnspan=2)
        password_entry.grid(column=1,row=1,columnspan=2)
        register_button.grid(row=2,column=1)

        entry_frame.pack(side="top")

