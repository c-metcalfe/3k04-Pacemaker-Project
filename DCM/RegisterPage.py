import tkinter as tk
import os
from Dashboard import DashboardClass
from User import UserClass

#ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..')) # this is needed to create new files in the users folder with an absolute path

CONST_Max_user_count = 10


class RegisterPageClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Register Page", font = ('Times New Roman',20, "bold") )
        self.controller = controller
        label.pack(pady=20)

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
        register_button = tk.Button(entry_frame, text="Register new User",
                                 command=lambda: self.attempt_register(username_entry.get(),
                                                                       password_entry.get(), 
                                                                       message_box))

        username_label.grid(column=0,row=0)
        password_label.grid(column=0,row=1)
        username_entry.grid(column=1,row=0,columnspan=2)
        password_entry.grid(column=1,row=1,columnspan=2)
        register_button.grid(row=2,column=1)
        message_box.grid(row=3, column=0,columnspan=3)

        entry_frame.pack(side="top")

    def attempt_register(self, username, password, message_box):  
        message_box.config(text="")
        print("register?")
        # if not too many users make a new user file in the Users folder, add appropriate info, set all parameters to default values
        users_count = 0
        users_folder_path = os.path.join("DCM","Users")

        for path in os.listdir(users_folder_path):  # count number of existing user files in the user folder
            if os.path.isfile(os.path.join(users_folder_path, path)): # check if current path is a file or folder
                users_count += 1
            if("{}.txt".format(username) == path): # if user already exists in users folder
                message_box.config(text="Error: User already exists")
                return(False) 
        
        if users_count >= CONST_Max_user_count:   
            
            message_box.config(text="Error: Maximum of 10 Users already created")
            return False
        
        self.createUserFile(username,password)
        # make new user file to store user data
        
        potential_user = UserClass(username)
        self.controller.load_dashboard(potential_user)
        self.controller.show_frame(DashboardClass)


    def createUserFile(self, username,password):
        filename = "{}.txt".format(username)
        file_path = os.path.join("DCM","Users",filename)

        new_user_file = open(file_path,"w")  
        new_user_file.write("{}\n".format(username))  
        new_user_file.write("{}\n".format(password))

        # write default parameters
        new_user_file.write("60\n") # default pacing rate is 60 bpm
        new_user_file.write("1\n") # default mode is 1 for AOO
        new_user_file.write("0.4\n") # default ventricular pulse width (ms)
        new_user_file.write("2.5\n") # default ventricular amplitude (V)
        new_user_file.write("0.4\n") # default atrial pulse width (ms)
        new_user_file.write("2.5\n") # default atrial amplitude (V)
        new_user_file.write("120\n") # default upper rate limit (ppm)
        new_user_file.write("60\n") # default lower rate limit (ppm)
        new_user_file.write("250\n") # default ARP (ms)
        new_user_file.write("320\n") # default VRP (ms)
        new_user_file.write("250\n") # default PVARP (ms)
        new_user_file.write("0\n") # default hysteresis rate limit (0 or same as LRL)
        new_user_file.close()



