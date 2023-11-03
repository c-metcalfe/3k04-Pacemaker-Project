import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np


from tkinter import *

data = []

def start_plot():
    data.append(np.random.uniform(0, 5))
    ax.plot(data, color="blue")
    canvas.draw_idle()
    main_window.after(100, start_plot) # in milliseconds, 1000 for 1 second
    

main_window = Tk()
main_window.configure(background='light blue')

main_window.title("ECG-LArdmon")
main_window.geometry('800x700')
main_window.resizable(width=False, height=False)




plotting_frame = LabelFrame(main_window, text='Real Time', bg='white', width=300, height=440, bd=5, relief=SUNKEN)
controls_frame = LabelFrame(main_window, text='Controls', background='light grey', height=150)

controls_frame.pack(fill='both', expand='1', side=TOP, padx=20, pady=10)
plotting_frame.pack(fill='both', expand='yes', side=BOTTOM, padx=20)


start_button = Button(controls_frame, text='Start Monitoring', width=16, height=2, borderwidth=3, command=start_plot)
start_button.pack(side=LEFT, padx=26)

exit_button = Button(controls_frame, text='Close', width=10, height=2, borderwidth=3, command=main_window.destroy)
exit_button.pack(side=RIGHT, padx=26)




fig = Figure()
ax = fig.add_subplot(111)
ax.set_title("Electrocadiogram")
ax.set_xlabel("Time(Sec)")
ax.set_ylabel("Voltage(mV)")
ax.set_xlim(0, 200)
ax.set_ylim(-0.5, 6)
ax.grid(which='major', color='#666666', linestyle='-')
ax.minorticks_on()
ax.grid(which='minor', color='#666666', linestyle='-', alpha=0.2)
canvas = FigureCanvasTkAgg(fig, master=plotting_frame)
canvas.get_tk_widget().place(x = 0, y = 0, width = 600, height = 420)
canvas.draw()

main_window.mainloop()