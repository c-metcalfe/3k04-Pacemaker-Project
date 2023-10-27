import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
import serial as sr
import time
import random

class egramPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.keepPlotting=False
        startBtn = tk.Button(self, text="Start plotting", command =lambda: self.startButtonFunc())
        startBtn.pack(side="top")


        self.atrData = []
        self.ventData = []

        atriumPlotFrame = tk.LabelFrame(self, text='Atrium', bg='white', width=300, height=150)
        atriumPlotFrame.pack(side="top")
        ventPlotFrame = tk.LabelFrame(self, text='Ventricle', bg='white', width=300, height=150)
        ventPlotFrame.pack(side="top")

        atrFig = Figure()
        ventFig = Figure()

        self.ax = atrFig.add_subplot(111)
        self.ax.set_title("Atrium Electrocadiogram")
        self.ax.set_xlabel("Time(Sec)")
        self.ax.set_ylabel("Voltage(mV)")
        self.ax.set_xlim(0, 200)
        self.ax.set_ylim(-0.5, 6)

        self.vx = ventFig.add_subplot(111)
        self.vx.set_title("Ventricle Electrocadiogram")
        self.vx.set_xlabel("Time(Sec)")
        self.vx.set_ylabel("Voltage(mV)")
        self.vx.set_xlim(0, 200)
        self.vx.set_ylim(-0.5, 6)

        self.atrCanvas = FigureCanvasTkAgg(atrFig, master=atriumPlotFrame)
        self.ventCanvas = FigureCanvasTkAgg(ventFig, master=ventPlotFrame)

        self.atrCanvas.get_tk_widget().pack(side="top")
        self.ventCanvas.get_tk_widget().pack(side="top")
        self.atrCanvas.draw()
        self.ventCanvas.draw()

    def startButtonFunc(self):
        self.keepPlotting =True
        self.updatePlots()

    def updatePlots(self):
        
        a = random.random() # TODO implement serial here
        
        self.atrData.append(a)
        self.ventData.append(a)

        # self.ax.cla()
        # self.vx.cla()
        self.ax.plot(self.atrData, color="blue")
        self.vx.plot(self.ventData, color="blue")

        self.ventCanvas.draw_idle()
        self.atrCanvas.draw_idle()
        if self.keepPlotting:
            self.after(200, self.updatePlots)
        else:
            return
        
    def stopPlotting(self):
        self.keepPlotting=False

    
