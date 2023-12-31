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
        startBtn.pack(side="top")
        stopBtn.pack(side="top")
        legendLabel = tk.Label(btnBox, text = "red: Natural Paces   blue: Delivered Paces")
        legendLabel.pack(side="top")
        btnBox.pack(side="top")


        self.msg_label = tk.Label(self, text = "")
        self.msg_label.pack(side="top")

        self.startTime = time.time_ns()/1000000
        self.atrData = [0] *100
        self.ventData = [0] *100
        self.atrDataN = [0] *100
        self.ventDataN = [0] *100

        self.times = list(range(0, 10000, 100))

        self.atrFrame = tk.LabelFrame(self, text='Atrium', bg='white', width=200, height=100)
        self.ventFrame = tk.LabelFrame(self, text='Ventricle', bg='white', width=200, height=100)
        
        

        self.atrFig = Figure(figsize=(6,3))
        self.ventFig = Figure(figsize=(6,3))
        
        
        self.atrFig.suptitle("Atrium Electrogram")
        self.atrFig.supxlabel("Time (ms)", y=0)
        self.atrFig.supylabel("Voltage")
        self.ax = self.atrFig.add_subplot(111) 
        
        self.ax.set

        self.atrFig.subplots_adjust(bottom=0.25)
        self.ax.set_xlim(0, 10)  ## 2000 values stored, new value retrieved every 5 ms, 2000*5mS=10s
        self.ax.set_ylim(-0.5, 6)
        

        self.ventFig.tight_layout()
        self.ventFig.suptitle("Ventricle Electrogram")
        self.ventFig.supxlabel("Time (ms)", y=0)
        self.ventFig.supylabel("Voltage")
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
        self.startTime = time.time_ns()/1000000
        self.atrData = [0] *100
        self.ventData = [0] *100
        self.atrDataN = [0] *100
        self.ventDataN = [0] *100

        self.times = (list(range(0, -10000, -100)))
        self.keepPlotting =True
        self.user.serial.ser.reset_input_buffer()
        self.updatePlots()

    def stopPlotting(self):
        self.keepPlotting=False

    def backBtnFunc(self):
        self.keepPlotting=False
        self.controller.show_dashboard()

  
    def updatePlots(self):

        #try:
        if self.user.serial.ser.in_waiting >= 5:
            a = self.user.serial.ser.read(5)
            atrN = a[0]
            atr = a[1]
            ventN = a[2]
            vent = a[3]
            print(a)
        else:
            atr = 0
            vent = 0
            atrN = 0
            ventN = 0


        # except:
        #     self.msg_label.config(text="Connection Failed", bg="red")
        #     return
        self.msg_label.config(text="Device connected", bg="light green")
        # atr = 3*random.random()**2 
        # vent = 3*random.random()**2 

        self.atrData.insert(0,atr)
        self.ventData.insert(0,vent)
        self.atrDataN.insert(0,atrN)
        self.ventDataN.insert(0,ventN)
        self.times.insert(0, (time.time_ns()/1000000)-self.startTime)  # reverse here to make the graph scroll the other way aand not have negative numbers

        self.ventData.pop()
        self.atrData.pop()
        self.ventDataN.pop()
        self.atrDataN.pop()
        self.times.pop()

        # print(self.atrData)
        # print(self.ventData)

        self.ax.cla()
        self.vx.cla()
        self.ax.plot(self.times, self.atrData, color="blue")
        self.ax.plot(self.times, self.atrDataN, color="red")

        self.vx.plot(self.times, self.ventData, color="blue")
        self.vx.plot(self.times, self.ventDataN, color="red")

        self.atrCanvas.draw_idle()
        self.ventCanvas.draw_idle()

        
        if self.keepPlotting:
            # for i in range (3):
            #     time.sleep(0.005)
            #     if self.user.serial.ser.in_waiting >= 5: # if new data
            #         print("here")
            #         self.after(5, self.updatePlots)
            self.user.serial.ser.reset_input_buffer()
            self.after(15, self.updatePlots)

            
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
