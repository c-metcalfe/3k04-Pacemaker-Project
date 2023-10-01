import tkinter as tk
from User import UserClass

class DashboardClass(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Dashboard")
        label.pack(padx=10, pady=10)
        self.user=None

        back_button = tk.Button(
            self,
            text="Back",
            command=lambda: self.lower()
        )
        back_button.pack(side="top", anchor="nw")

    def set_user(self,user):
        self.user = user

    def load_user_info(self):
        if not self.user: 
            return
        user_info_container = tk.Frame(self)
        name_label = tk.Label(user_info_container,text = "Current user: {}".format(self.user.getUsername()))
        name_label.grid(row=0,column=0)

        user_info_container.pack(side="top")

    