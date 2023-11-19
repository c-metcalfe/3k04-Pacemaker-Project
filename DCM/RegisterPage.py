import tkinter as tk
import os
from Dashboard import DashboardClass
from User import UserClass

#ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..')) # this is needed to create new files in the users folder with an absolute path

CONST_Max_user_count = 10


class RegisterPageClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Register Page", font = ('Times New Roman', 20, "bold") )
        self.controller = controller
        label.pack(pady=20)
        
        label1=tk.Label(self, text = "Create new account", font = ('Times New Roman', 15, "normal"))
        label1.pack(pady=2)

        back_button = tk.Button(
            self,
            text="Back",
            command=lambda: self.lower()
        )
        back_button.pack(side="top", anchor="nw")

        entry_frame = tk.Frame(self)
        username_label = tk.Label(entry_frame, text="Username:")
        password_label = tk.Label(entry_frame, text="Password:")
        self.username_entry = tk.Entry(entry_frame)
        self.password_entry = tk.Entry(entry_frame)
        message_box = tk.Label(entry_frame, text="Please enter your username and password")
        register_button = tk.Button(entry_frame, text="Register new User",command=lambda: self.attempt_register(self.username_entry.get(),self.password_entry.get(), message_box))

        username_label.grid(column=0,row=0)
        password_label.grid(column=0,row=1)
        self.username_entry.grid(column=1,row=0,columnspan=2)
        self.password_entry.grid(column=1,row=1,columnspan=2)
        register_button.grid(row=2,column=1)
        message_box.grid(row=3, column=0,columnspan=3)

        entry_frame.pack(side="top")

    def attempt_register(self, username, password, message_box):  
        message_box.config(text=" ")
        print("register?")
        # if not too many users make a new user file in the Users folder, add appropriate info, set all parameters to default values
        users_count = 0
        users_folder_path = os.path.join("DCM","Users")

        if (" " in username or username == ""):
            message_box.config(text="Error: Invalid Username")
            return(False) 

        for path in os.listdir(users_folder_path):  # count number of existing user files in the user folder
            users_count += 1
            if("{}".format(username) == path): # if user already exists in users folder
                message_box.config(text="Error: User already exists")
                return(False) 
        
        if users_count >= CONST_Max_user_count:   
            
            message_box.config(text="Error: Maximum of 10 Users already created")
            return False
        if not self.createUserFolder(username):
            message_box.config(text="Error: New user folder could not be created")
            return False

        # make new user file to store user data
        if not self.createUserFile(username,password):
            message_box.config(text="Error: New user file could not be created")
            return False
        
        potential_user = UserClass(username)
        if self.controller.load_dashboard(potential_user):
            self.password_entry.delete(0,len(self.password_entry.get()))
            self.username_entry.delete(0,len(self.username_entry.get())) 
            self.controller.set_egram_user(potential_user)
            self.controller.show_frame(DashboardClass)
            self.controller.chooseMode()

            return True
        return False

    def createUserFolder(self, username):
        user_folder_path = os.path.join("DCM","Users","{}".format(username))
        try:
            os.mkdir(user_folder_path)
            return True
        except:
            return False


    def createUserFile(self, username,password):
        try:
            filename = "{}.txt".format(username)
            file_path = os.path.join("DCM","Users", username, filename)

            new_user_file = open(file_path,"w")  
            new_user_file.write("{}\n".format(username))  
            new_user_file.write("{}\n".format(password))

            # write default parameters
            new_user_file.write("60\n") # default pacing rate is 60 bpm
            new_user_file.write("255\n") # default mode is 255 for no mode
            new_user_file.write("1\n") # default ventricular pulse width (ms)
            new_user_file.write("5.0\n") # default ventricular amplitude (V)
            new_user_file.write("1\n") # default atrial pulse width (ms)
            new_user_file.write("5.0\n") # default atrial amplitude (V)
            new_user_file.write("120\n") # default upper rate limit (ppm)
            new_user_file.write("60\n") # default lower rate limit (ppm)
            new_user_file.write("250\n") # default ARP (ms)
            new_user_file.write("320\n") # default VRP (ms)
            new_user_file.write("250\n") # default PVARP (ms)
            new_user_file.write("0\n") # default hysteresis rate limit (0 or same as LRL)
            new_user_file.write("0.5\n") # default sensitivity
            new_user_file.write("3\n") # default activity threshold
            new_user_file.write("30\n") # default reactionTime
            new_user_file.write("8\n") # default responseFactor
            new_user_file.write("5\n") # default recoveryTime
            new_user_file.write("120\n") # default maxSensorRate

            new_user_file.close()
            return True
        except:
            return False



