# Main function to call GUI class when run
from tkinter import *
from tkinter import ttk
import GUI

def on_closing():  # closes seral port when window is closed
    user = test.frames[GUI.DashboardClass].user
    if user: # if signed in
        if user.serial and user.serial.ser.is_open: # serial created and serial port still open
            user.serial.ser.close()
            print("closed serial port")
    
    test.destroy()


if __name__ == "__main__": # Run Main loop
    test = GUI.GUI()
    test.protocol("WM_DELETE_WINDOW", on_closing)
    test.mainloop()
    