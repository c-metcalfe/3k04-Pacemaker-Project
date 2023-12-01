# GUI class

# class structure based on https://gist.github.com/dat-adi/baf5a4a64358a5f1d13452ef7b584cbc

import tkinter as tk 
from tkinter import ttk
from WelcomePage import WelcomePageClass
from LoginPage import LoginPageClass
from RegisterPage import RegisterPageClass
from WelcomePage import WelcomePageClass
from Dashboard import DashboardClass
from egramPage import egramPage
##import SerialComm

class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) # when the GUI is created, pass args to tkinter default init function
        self.wm_title("DCM Application")
        #self.wm_geometry("1000x750")
        # self.attributes('-fullscreen', True)
        width= self.winfo_screenwidth()               
        height= self.winfo_screenheight()               
        self.geometry("%dx%d" % (width, height))

        container = tk.Frame(self, height=4000, width=6000)
        container.pack(side="top", fill="both", expand=True)
        
        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        frame = self.frames 

        for F in (WelcomePageClass, LoginPageClass, RegisterPageClass, DashboardClass, egramPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Using a method to switch frames
        self.show_frame(WelcomePageClass)
    
    def show_frame(self, content):
        frame = self.frames[content]
        # raises the current frame to the top
        frame.tkraise()
        
    def show_login(self):
        self.show_frame(LoginPageClass)

    def show_dashboard(self):
        self.show_frame(DashboardClass)
        
    def show_egram(self):
        self.show_frame(egramPage)

    def show_welcome(self):
        self.show_frame(WelcomePageClass)

    def load_dashboard(self, user):
        dashboard = self.frames[DashboardClass]
        dashboard.set_user(user)
        dashboard.load_user_info()
        dashboard.changeMode(dashboard.user.mode, dashboard.changeParamMessageBox)
        
        return True
    
    def set_egram_user(self, user):
        egram = self.frames[egramPage]
        egram.user = user

    def logout(self):
        try:  # TODO test with board
            user = self.frames[egramPage].user
            if user.serial and user.serial.ser.is_open: # serial created and serial port still open
                user.serial.ser.close()
        except: # if already closed of never opened
            pass
        self.frames[egramPage].user = None
        self.frames[DashboardClass].user = None
    
    def chooseMode(self):
        dashboard = self.frames[DashboardClass]
        dashboard.emptyTable()
        dashboard.addModeToTable(0)
        dashboard.changeParamMessageBox.config(text="")
        dashboard.modeLabel.config(text="Choose a Pacing Mode")