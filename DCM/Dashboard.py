import tkinter as tk
from User import UserClass

class DashboardClass(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.nameLabel = tk.Label(self, text="Dashboard")
        self.nameLabel.pack(padx=10, pady=10)

        #TODO add labels for all necessary user info ie:
        # self.heartRateLabel = tk.Label(self, text = "fjenfeuief")...
        self.user=None

        back_button = tk.Button(
            self,
            text="Back",
            command=lambda: self.lower()
        )
        back_button.pack(side="top", anchor="nw")

    def set_user(self,user: UserClass):
        self.user = user

    def load_user_info(self):
        if not self.user: 
            return
        
        self.nameLabel.config(text = "Current user: {}".format(self.user.getUsername()))
        # TODO add user info to screen ie:
        # self.heartRateLabel.config(text="Heart rate: {}".format(self.user.heartRate))
        


    