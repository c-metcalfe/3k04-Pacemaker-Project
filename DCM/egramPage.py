import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
import serial as sr
import time
import random

class egramPage(tk.Frame):
    def __init__(self, parent, controller, user=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.user = user

        self.keepPlotting=False
        backBtn = tk.Button(self, text="Back", command =lambda: self.backBtnFunc())
        backBtn.pack(side="top", anchor="nw")
        startBtn = tk.Button(self, text="Start plotting", command =lambda: self.startButtonFunc())
        startBtn.pack(side="top")

        self.msg_label = tk.Label(self, text = "")
        self.msg_label.pack(side="top")

        self.atrData = []
        self.ventData = []

        self.atrFrame = tk.LabelFrame(self, text='Atrium', bg='white', width=200, height=100)
        self.ventFrame = tk.LabelFrame(self, text='Ventricle', bg='white', width=200, height=100)
        
        

        self.atrFig = Figure(figsize=(6,2))
        self.ventFig = Figure(figsize=(6,2))
        

        self.ax = self.atrFig.add_subplot(111) 
        self.ax.set_title("Atrium Electrocadiogram")
        self.ax.set_xlabel("Time(Sec)")
        self.ax.set_ylabel("Voltage(mV)")
        self.ax.set_xlim(0, 200)
        self.ax.set_ylim(-0.5, 6)

        self.vx = self.ventFig.add_subplot(111) 
        self.vx.set_title("Ventricle Electrocadiogram")
        self.vx.set_xlabel("Time(Sec)")
        self.vx.set_ylabel("Voltage(mV)")
        self.vx.set_xlim(0, 200)
        self.vx.set_ylim(-0.5, 6)

        self.atrCanvas = FigureCanvasTkAgg(self.atrFig, master=self.atrFrame)
        self.ventCanvas = FigureCanvasTkAgg(self.ventFig, master=self.ventFrame)

        self.atrCanvas.get_tk_widget().grid(row=1,column=1, sticky="nsew")
        self.ventCanvas.get_tk_widget().grid(row=1,column=1, sticky="nsew")

        self.atrCanvas.draw()
        self.ventCanvas.draw()
        
        
        
        btnBox = tk.Frame(self)
        ventBtn = tk.Button(btnBox,text="Ventricle", command=lambda: self.changeView("Ventricle"))
        atrBtn = tk.Button(btnBox,text="Atrium", command=lambda: self.changeView("Atrium"))
        bothBtn = tk.Button(btnBox,text="Both", command=lambda: self.changeView("Both"))

        ventBtn.pack(side="left")
        atrBtn.pack(side="left")
        bothBtn.pack(side="left")
        btnBox.pack(side="top")



        self.atrFrame.pack(side="top")
        self.ventFrame.pack(side="top")

    def startButtonFunc(self):
        self.keepPlotting =True
        self.updatePlots()

    def backBtnFunc(self):
        self.keepPlotting=False
        self.controller.show_dashboard()

  
    def updatePlots(self):

        try:
            a = self.user.serial.read(5)

        except:
            self.msg_label.config(text="No device connection", bg="red")
            return
        self.msg_label.config(text="Device connectted", bg="light green")
        atr = a[1]
        vent = a[2]

        self.atrData.insert(0,atr)
        self.ventData.insert(0,vent)

        # self.ax.cla()
        # self.vx.cla()
        self.ax.plot(self.atrData, color="blue")
        self.vx.plot(self.ventData, color="blue")

        self.atrCanvas.draw_idle()
        self.ventCanvas.draw_idle()
        if self.keepPlotting:
            self.after(200, self.updatePlots)
        else:
            return
        
  
    def changeView(self, view):
        #view = self.selected.get()
        self.atrFrame.pack_forget()
        self.ventFrame.pack_forget()
        print("deleted")
        if view == "Atrium":
            self.atrFrame.pack(side="top")
        elif view == "Ventricle":
            self.ventFrame.pack(side="top")
        else:
            self.atrFrame.pack(side="top")
            self.ventFrame.pack(side="top")
