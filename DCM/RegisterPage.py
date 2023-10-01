import tkinter as tk
import os
from Dashboard import DashboardClass

#ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..')) # this is needed to create new files in the users folder with an absolute path

CONST_Max_user_count = 10


class RegisterPageClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Register Page")
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
        register_button = tk.Button(entry_frame, text="Register new User",
                                 command=lambda: self.attempt_register(username_entry.get(),password_entry.get()))

        username_label.grid(column=0,row=0)
        password_label.grid(column=0,row=1)
        username_entry.grid(column=1,row=0,columnspan=2)
        password_entry.grid(column=1,row=1,columnspan=2)
        register_button.grid(row=2,column=1)

        entry_frame.pack(side="top")

    def attempt_register(self, username, password):  # TODO prevent creation of duplicate users
        print("register?")
        # if not too many users make a new user file in the Users folder, add appropriate info, set all parameters to default values
        users_count = 0
        users_folder_path = "/Users"
        for path in os.listdir(users_folder_path):  # count number of existing user files in the user folder
            if os.path.isfile(os.path.join(users_folder_path, path)): # check if current path is a file or folder
                users_count += 1
        
        if users_count >= CONST_Max_user_count:   
            print("Error: Maximum of 10 Users already created")
            return False
        
        # make new user file to store user data
        filename = "{}.txt".format(username)
        file_path = os.path.join("DCM","Users",filename)

        new_user_file = open(file_path,"w")  
        new_user_file.write("{}\n".format(username))  
        new_user_file.write("{}\n".format(password))  


        # TODO write default parameters
        new_user_file.close()
        self.controller.show_frame(DashboardClass) # or should we make



