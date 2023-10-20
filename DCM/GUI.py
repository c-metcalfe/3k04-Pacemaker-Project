# GUI class

# class structure based on https://gist.github.com/dat-adi/baf5a4a64358a5f1d13452ef7b584cbc

import tkinter as tk 
from tkinter import ttk
from WelcomePage import WelcomePageClass
from LoginPage import LoginPageClass
from RegisterPage import RegisterPageClass
from WelcomePage import WelcomePageClass
from Dashboard import DashboardClass

class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) # when the GUI is created, pass args to tkinter default init function
        self.wm_title("DCM Application")
        self.wm_geometry("1000x600")
        
        container = tk.Frame(self, height=4000, width=6000)
        container.pack(side="top", fill="both", expand=True)
        
        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        frame = self.frames 

        for F in (WelcomePageClass, LoginPageClass, RegisterPageClass, DashboardClass):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Using a method to switch frames
        self.show_frame(WelcomePageClass)
    
    def show_frame(self, content):
        frame = self.frames[content]
        # raises the current frame to the top
        frame.tkraise()

    def show_login(self): # avoids circular imports
        self.show_frame(LoginPageClass)

    def load_dashboard(self, user):
        dashboard = self.frames[DashboardClass]
        dashboard.set_user(user)
        dashboard.load_user_info()