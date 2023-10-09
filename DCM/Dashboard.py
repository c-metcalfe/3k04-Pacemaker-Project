import tkinter as tk
from User import UserClass

class DashboardClass(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)

        back_button = tk.Button(self,text="Back", command=lambda: self.backButtonCommand())
        back_button.pack(side="top", anchor="nw")
        
        self.nameLabel = tk.Label(self, text="Dashboard")
        self.nameLabel.pack(padx=10, pady=10)
        
        self.parametersFrame = tk.Frame(self)
        
        self.changeParamMessageBox = tk.Label(self,font=('bold'),text="Enter values then use button to change indicated parameters")

        #headers
        self.labelHeader = tk.Label(self.parametersFrame, text="Parameter",font=("bold"))
        self.entryHeader = tk.Label(self.parametersFrame, text="Entry",font=("bold"))
        self.conditionHeader = tk.Label(self.parametersFrame, text="Conditions for Entry",font=("bold"))

        self.labelHeader.grid(row=0,column=0)
        self.entryHeader.grid(row=0,column=1)
        self.conditionHeader.grid(row=0,column=3)

        #pacing rate
        self.rateLabel = tk.Label(self.parametersFrame,text="Pacing Rate: ")
        self.rateLabel2 = tk.Label(self.parametersFrame,text="Must be an integer between lower and upper rate limits.")
        self.rateEntry = tk.Entry(self.parametersFrame)
        self.changeRateBtn = tk.Button(self.parametersFrame, text="Change rate", 
                                    command=lambda: self.changePaceRate(self.rateEntry.get(), self.changeParamMessageBox))
        self.rateLabel.grid(row=1,column=0)
        self.rateEntry.grid(row=1, column=1)
        self.changeRateBtn.grid(row=1,column=2,sticky="W")
        self.rateLabel2.grid(row=1,column=3,sticky="W")

        #pacing mode
        self.modeLabel = tk.Label(self.parametersFrame,text="Mode:")
        self.modeLabel2 = tk.Label(self.parametersFrame,text="Must me a valid Mode name (AOO, VOO, AII, VII) or mode number (1-4)")
        self.modeEntry = tk.Entry(self.parametersFrame)
        self.changeModeBtn = tk.Button(self.parametersFrame, text="Change Mode",
                                    command=lambda: self.changeMode(self.modeEntry.get(), self.changeParamMessageBox))
        self.modeLabel.grid(row=2,column=0)
        self.modeEntry.grid(row=2, column=1)
        self.changeModeBtn.grid(row=2,column=2,sticky="W")
        self.modeLabel2.grid(row=2,column=3,sticky="W")

        #ventricular pulse width
        self.ventPWLabel = tk.Label(self.parametersFrame,text="Ventricular Pulse Width: ")
        self.ventPWLabel2 = tk.Label(self.parametersFrame,text="Must be a number in the range [0.3, 1.9] with one decimal place")
        self.ventPWEntry = tk.Entry(self.parametersFrame)
        self.changeVentPWBtn = tk.Button(self.parametersFrame, text="Change Ventricular Pulse Width",
                                    command=lambda: self.changeVentPW(self.ventPWEntry.get(), self.changeParamMessageBox))
        self.ventPWLabel.grid(row=3,column=0)
        self.ventPWEntry.grid(row=3, column=1)
        self.changeVentPWBtn.grid(row=3,column=2,sticky="W")
        self.ventPWLabel2.grid(row=3,column=3,sticky="W")
        
        # ventricular amplitude
        self.ventAmpLabel = tk.Label(self.parametersFrame,text="Ventricular amplitude: ")
        self.ventAmpLabel2 = tk.Label(self.parametersFrame,text="Options are: [2.5,3.0,3.5,4.0,4.5,5.0]")
        self.ventAmpEntry = tk.Entry(self.parametersFrame)
        self.changeVentAmpBtn = tk.Button(self.parametersFrame, text="Change VA",
                                    command=lambda: self.changeVentAmp(self.ventAmpEntry.get(), self.changeParamMessageBox))
        self.ventAmpLabel.grid(row=4,column=0)
        self.ventAmpEntry.grid(row=4, column=1)
        self.changeVentAmpBtn.grid(row=4,column=2,sticky="W")
        self.ventAmpLabel2.grid(row=4,column=3,sticky="W")

        #Atrial pulse width
        self.atrialPWLabel = tk.Label(self.parametersFrame,text=" Atrial Pulse Width: ")
        self.atrialPWLabel2 = tk.Label(self.parametersFrame,text="Must be a number in the range [0.3, 1.9] with one decimal place")
        self.atrialPWEntry = tk.Entry(self.parametersFrame)
        self.changeAtrialPWBtn = tk.Button(self.parametersFrame, text="Change Atrial Pulse Width",
                                    command=lambda: self.changeAtrialPW(self.atrialPWEntry.get(), self.changeParamMessageBox))
        self.atrialPWLabel.grid(row=5,column=0)
        self.atrialPWEntry.grid(row=5, column=1)
        self.changeAtrialPWBtn.grid(row=5,column=2,sticky="W")
        self.atrialPWLabel2.grid(row=5,column=3,sticky="W")

        #Atrial amplitude
        self.atrialAmpLabel = tk.Label(self.parametersFrame,text=" Atrial Amplitude: ")
        self.atrialAmpLabel2 = tk.Label(self.parametersFrame,text="Options are: [2.5,3.0,3.5,4.0,4.5,5.0]")
        self.atrialAmpEntry = tk.Entry(self.parametersFrame)
        self.changeAtrialAmpBtn = tk.Button(self.parametersFrame, text="Change Atrial Amplitude",
                                    command=lambda: self.changeAtrialAmp(self.atrialAmpEntry.get(), self.changeParamMessageBox))
        self.atrialAmpLabel.grid(row=6,column=0)
        self.atrialAmpEntry.grid(row=6, column=1)
        self.changeAtrialAmpBtn.grid(row=6,column=2,sticky="W")
        self.atrialAmpLabel2.grid(row=6,column=3,sticky="W")
        
        #upperRateLimit
        self.URLLabel = tk.Label(self.parametersFrame,text=" Upper Rate limit: ")
        self.URLLabel2 = tk.Label(self.parametersFrame,wraplength="400", justify="left",
                                  text="Must be an interger in the range [50,175] that is divisible by 5 and greater than the current pacing rate")
        self.URLEntry = tk.Entry(self.parametersFrame)
        self.changeURLBtn = tk.Button(self.parametersFrame, text="Change the URL(upper rate width)",
                                    command=lambda: self.changeURL(self.URLEntry.get(), self.changeParamMessageBox))
        self.URLLabel.grid(row=7,column=0)
        self.URLEntry.grid(row=7, column=1)
        self.changeURLBtn.grid(row=7,column=2,sticky="W")
        self.URLLabel2.grid(row=7,column=3,sticky="W")

        #lower rate limit
        self.LRLLabel = tk.Label(self.parametersFrame,text="Lower Rate limit: ")
        self.LRLLabel2 = tk.Label(self.parametersFrame,wraplength="400", justify="left",
                                  text="Must be an integer in the range [30,175] that is divisible by 5, less than the upper rate limit, and less than the current pacing rate")
        self.LRLEntry = tk.Entry(self.parametersFrame)
        self.changeLRLBtn = tk.Button(self.parametersFrame, text="Change LRL(Lower rate limit)",
                                    command=lambda: self.changeLRL(self.LRLEntry.get(), self.changeParamMessageBox))
        self.LRLLabel.grid(row=8,column=0)
        self.LRLEntry.grid(row=8, column=1)
        self.changeLRLBtn.grid(row=8,column=2,sticky="W")
        self.LRLLabel2.grid(row=8,column=3,sticky="W")
        
        #hysteresisRateLimit
        self.HRLLabel = tk.Label(self.parametersFrame,text="Hysteresis Rate Limit ")
        self.HRLLabel2 = tk.Label(self.parametersFrame,wraplength="400", justify="left",
                                  text="Must be 0 or an integer in the range [30,175] that is divisible by 5 and less than the upper rate limit")
        self.HRLEntry = tk.Entry(self.parametersFrame)
        self.changeHRLBtn = tk.Button(self.parametersFrame, text="Change Hysteresis Rate Limit",
                                    command=lambda: self.changeHRL(self.HRLEntry.get(), self.changeParamMessageBox))
        self.HRLLabel.grid(row=9,column=0)
        self.HRLEntry.grid(row=9, column=1)
        self.changeHRLBtn.grid(row=9,column=2,sticky="W")
        self.HRLLabel2.grid(row=9,column=3,sticky="W")
        
        #ARP
        self.ARPLabel = tk.Label(self.parametersFrame,text="ARP")
        self.ARPLabel2 = tk.Label(self.parametersFrame,wraplength="400",text="Must be an integer in the range [150, 500] that is divisible by 10")
        self.ARPEntry = tk.Entry(self.parametersFrame)
        self.changeARPBtn = tk.Button(self.parametersFrame, text="Change ARP",
                                    command=lambda: self.changeARP(self.ARPEntry.get(), self.changeParamMessageBox))
        self.ARPLabel.grid(row=10,column=0)
        self.ARPEntry.grid(row=10, column=1)
        self.changeARPBtn.grid(row=10,column=2,sticky="W")
        self.ARPLabel2.grid(row=10,column=3,sticky="W")
        
        #VRP
        self.VRPLabel = tk.Label(self.parametersFrame,text="VRP")
        self.VRPLabel2= tk.Label(self.parametersFrame,wraplength="400",text="Must be an integer in the range [150, 500] that is divisible by 10")
        self.VRPEntry = tk.Entry(self.parametersFrame)
        self.changeVRPBtn = tk.Button(self.parametersFrame, text="Change VRP",
                                    command=lambda: self.changeVRP(self.VRPEntry.get(), self.changeParamMessageBox))
        self.VRPLabel.grid(row=11,column=0)
        self.VRPEntry.grid(row=11, column=1)
        self.changeVRPBtn.grid(row=11,column=2,sticky="W")
        self.VRPLabel2.grid(row=11,column=3,sticky="W")
        
        #PVARP
        self.PVARPLabel = tk.Label(self.parametersFrame,text="PVARP:")
        self.PVARPLabel2= tk.Label(self.parametersFrame,wraplength="400",text="Must be an integer in the range [150, 500] that is divisible by 10")
        self.PVARPEntry = tk.Entry(self.parametersFrame)
        self.changePVARPBtn = tk.Button(self.parametersFrame, text="Change PVARP",
                                    command=lambda: self.changePVARP(self.PVARPEntry.get(), self.changeParamMessageBox))
        self.PVARPLabel.grid(row=12,column=0)
        self.PVARPEntry.grid(row=12, column=1)
        self.changePVARPBtn.grid(row=12,column=2,sticky="W")
        self.PVARPLabel2.grid(row=12,column=3,sticky="W")
        
        
        

        #TODO add labels for all necessary user info ie:
        # self.heartRateLabel = tk.Label(self, text = "fjenfeuief")...
        self.parametersFrame.pack(side="top")
        self.changeParamMessageBox.pack(side="top",pady=20)
        
        self.user=None

        

    def backButtonCommand(self):
        self.lower()
        self.user = None
        
        ## change pacerate Button
    def changePaceRate(self, rate, message_box):
        if (self.user.setPacingRate(rate)):
            message_box.config(text="Set pacing rate",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid pacing rate",fg="red")
        ## MODE CHANGE Button 
    def changeMode(self, mode, message_box):
        if (self.user.setMode(mode)):
            message_box.config(text="Set Mode",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid Mode",fg="red")
        ## change ventPW BUTTON
    def changeVentPW(self, ventPW, message_box):
        if (self.user.setPacingRate(ventPW)):
            message_box.config(text="Set ventricular pulse width",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid ventricular pulse width",fg="red")
        
        ## change ventAmp BUTTON
    def changeVentAmp(self, ventAmp, message_box):
        if (self.user.setventAmp(ventAmp)):
            message_box.config(text="Set ventAmp",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid ventAmp",fg="red")
            
        ## Change atrial pulse width button
    def changeAtrialPW(self, atrialPW, message_box):
        if (self.user.setatrialPW(atrialPW)):
            message_box.config(text="Set Atrial Pulse Width",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid atrialPW",fg="red")
        
    #change atrial amp button
    def changeAtrialAmp(self, atrialAmp, message_box):
        if (self.user.setatrialPW(atrialAmp)):
            message_box.config(text="Set Atrial Amplitude",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid atrialPW",fg="red")
        
    
        #upperRateLimit
    def changeURL(self, URL, message_box):
        if (self.user.setUpperRateLimit(URL)):
            message_box.config(text="Set Upper Rate Limit",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: Upper Rate Limit",fg="red")
            
        
        # Lower Rate Limit
    def changeLRL(self, LRL, message_box):
        if (self.user.setLowerRateLimit(LRL)):
            message_box.config(text="set Lower Rate Limit",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid Lower Rate Limit",fg="red")
            
            
    #hysteresisRateLimit
    def changeHRL(self, HRL, message_box):
        if (self.user.setHysteresisRateLimit(HRL)):
            message_box.config(text="Set Hysteresis Rate Limit",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid HRL",fg="red")
    

    def changeARP(self, ARP, message_box):
        if (self.user.setARP(ARP)):
            message_box.config(text="set ARP",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid ARP",fg="red")
        
        
    def changeVRP(self, VRP, message_box):
        if (self.user.setVRP(VRP)):
            message_box.config(text="set VRP",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid VRP",fg="red")

    def changePVARP(self, PVARP, message_box):
        if (self.user.setARP(PVARP)):
            message_box.config(text="set PVARP",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid PVARP",fg="red")
        
    def set_user(self,user: UserClass):
        self.user = user

    def load_user_info(self):
        if not self.user: 
            return
        
        self.nameLabel.config(text = "Current user: {}".format(self.user.getUsername()), font = ('Times New Roman', 20, "bold"))
        self.nameLabel.pack(pady = 25)
        self.rateLabel.config(text = "Pacing Rate: {}".format(self.user.pacingRate))

        mode = self.user.mode
        if mode == 1: modeText = "AOO"
        elif mode == 2: modeText = "VOO"
        elif mode == 3: modeText = "AAI"
        elif mode == 4: modeText = "VVI"
        else: modeText = "ERROR"
        self.modeLabel.config(text = "Mode: {}".format(modeText))

        self.ventPWLabel.config(text="Ventricular Pulse Width: {}".format(self.user.ventPulseWidth))
        self.ventAmpLabel.config(text="Ventricular Amplitude: {}".format(self.user.ventAmplitude))
        self.atrialPWLabel.config(text="Atrial Pulse Width: {}".format(self.user.atrialPulseWidth))
        self.atrialAmpLabel.config(text="Atrial Amplitude: {}".format(self.user.atrialAmplitude))
        self.URLLabel.config(text="Upper Rate Limit: {}".format(self.user.upperRateLimit))
        self.LRLLabel.config(text="Lower Rate Limit: {}".format(self.user.lowerRateLimit))
        self.HRLLabel.config(text="Hysteresis Rate Limit: {}".format(self.user.hysteresisRateLimit))
        self.ARPLabel.config(text="Atrial Refractory Period: {}".format(self.user.ARP))
        self.VRPLabel.config(text="Ventricular Refractory Period: {}".format(self.user.VRP))
        self.PVARPLabel.config(text="Post-Ventricular Atrial Refractory Period: {}".format(self.user.ARP))

        #self.changeParamMessageBox.config(text="Enter values then use button to change indicated parameters")
        


        


    