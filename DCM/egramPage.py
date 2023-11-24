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
        btnBox = tk.Frame(self)
        startBtn = tk.Button(btnBox, text="Start plotting", command =lambda: self.startButtonFunc())
        stopBtn = tk.Button(btnBox, text="Stop plotting", command =lambda: self.stopPlotting())
        startBtn.pack(side="left")
        stopBtn.pack(side="right")
        btnBox.pack(side="top")


        self.msg_label = tk.Label(self, text = "")
        self.msg_label.pack(side="top")

        self.atrData = [0] *1000
        self.ventData = [0] *1000

        self.atrFrame = tk.LabelFrame(self, text='Atrium', bg='white', width=200, height=100)
        self.ventFrame = tk.LabelFrame(self, text='Ventricle', bg='white', width=200, height=100)
        
        

        self.atrFig = Figure(figsize=(6,3))
        self.ventFig = Figure(figsize=(6,3))
        
        
        self.atrFig.suptitle("Atrium Electrocadiogram")
        self.atrFig.supxlabel("Time(5 ms)", y=0)
        self.atrFig.supylabel("Voltage(mV)")
        self.ax = self.atrFig.add_subplot(111) 
        self.atrFig.subplots_adjust(bottom=0.25)
        self.ax.set_xlim(0, 10)  ## 2000 values stored, new value retrieved every 5 ms, 2000*5mS=10s
        self.ax.set_ylim(-0.5, 6)
        

        self.ventFig.tight_layout()
        self.ventFig.suptitle("Ventricle Electrocadiogram")
        self.ventFig.supxlabel("Time(5 ms)", y=0)
        self.ventFig.supylabel("Voltage(mV)")
        self.vx = self.ventFig.add_subplot(111) 
        self.ventFig.subplots_adjust(bottom=0.25)
        self.vx.set_xlim(0, 10)
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

    def stopPlotting(self):
        self.keepPlotting=False

    def backBtnFunc(self):
        self.keepPlotting=False
        self.controller.show_dashboard()

  
    def updatePlots(self):

        try:
            a = self.user.serial.ser.read(5)
            atr = a[1]
            vent = a[2]
            print(a)

        except:
            self.msg_label.config(text="Connection Failed", bg="red")
            return
        self.msg_label.config(text="Device connected", bg="light green")
        # atr = 3*random.random()**2 
        # vent = 3*random.random()**2 

        self.atrData.insert(0,atr)
        self.ventData.insert(0,vent)
        self.ventData.pop()
        self.atrData.pop()

        # print(self.atrData)
        # print(self.ventData)

        self.ax.cla()
        self.vx.cla()
        self.ax.plot(self.atrData, color="blue")
        self.vx.plot(self.ventData, color="blue")

        self.atrCanvas.draw_idle()
        self.ventCanvas.draw_idle()
        if self.keepPlotting:
            self.after(5, self.updatePlots)
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
