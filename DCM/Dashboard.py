import tkinter as tk
from User import UserClass

class DashboardClass(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.nameLabel = tk.Label(self, text="Dashboard")
        self.nameLabel.pack(padx=10, pady=10)
        
        self.parametersFrame = tk.Frame(self)
        
        self.changeParamMessageBox = tk.Label(self.parametersFrame,text="Enter values then use button to change indicated parameters")
        
        #pacing rate
        self.rateLabel = tk.Label(self.parametersFrame,text="Pacing Rate: ")
        self.rateEntry = tk.Entry(self.parametersFrame)
        self.changeRate = tk.Button(self.parametersFrame, text="Change rate", 
                                    command=lambda: self.changeRate(self.rateEntry.get(), self.changeParamMessageBox))
        self.rateLabel.grid(row=0,column=0)
        self.rateEntry.grid(row=0, column=1)
        self.changeRate.grid(row=0,column=2)

        #pacing mode
        self.modeLabel = tk.Label(self.parametersFrame,text="Mode:")
        self.modeEntry = tk.Entry(self.parametersFrame)
        self.changemode = tk.Button(self.parametersFrame, text="Change Mode",
                                    command=lambda: self.changemode(self.modeEntry.get(), self.changeParamMessageBox))
        self.modeLabel.grid(row=1,column=0)
        self.modeEntry.grid(row=1, column=1)
        self.changemode.grid(row=1,column=2)
        
        #ventricular pulse width
        self.ventPWLabel = tk.Label(self.parametersFrame,text="Ventricular Pulse Width: ")
        self.ventPWEntry = tk.Entry(self.parametersFrame)
        self.changeVentPW = tk.Button(self.parametersFrame, text="Change Ventricular Pulse Width",
                                    command=lambda: self.changeVentPW(self.ventPWEntry.get(), self.changeParamMessageBox))
        self.ventPWLabel.grid(row=2,column=0)
        self.ventPWEntry.grid(row=2, column=1)
        self.changeVentPW.grid(row=2,column=2)
        
        # ventricular amplitude
        self.ventAmpLabel = tk.Label(self.parametersFrame,text="Ventricular amplitude: ")
        self.ventAmpEntry = tk.Entry(self.parametersFrame)
        self.changeVentAmp = tk.Button(self.parametersFrame, text="Change VA",
                                    command=lambda: self.changeVentAmp(self.ventAmpEntry.get(), self.changeParamMessageBox))
        self.ventAmpLabel.grid(row=3,column=0)
        self.ventAmpEntry.grid(row=3, column=1)
        self.changeVentAmp.grid(row=3,column=2)

        #Atrial pulse width
        self.atrialPWLabel = tk.Label(self.parametersFrame,text=" Atrial Pulse Width: ")
        self.atrialPWEntry = tk.Entry(self.parametersFrame)
        self.changeAtrialPW = tk.Button(self.parametersFrame, text="Change Atrial Pulse Width",
                                    command=lambda: self.changeAtrialPW(self.atrialPWEntry.get(), self.changeParamMessageBox))
        self.atrialPWLabel.grid(row=4,column=0)
        self.atrialPWEntry.grid(row=4, column=1)
        self.changeAtrialPW.grid(row=4,column=2)

        #Atrial amplitude
        self.atrialAmpLabel = tk.Label(self.parametersFrame,text=" Atrial Amplitude: ")
        self.atrialAmpEntry = tk.Entry(self.parametersFrame)
        self.changeAtrialAmp = tk.Button(self.parametersFrame, text="Change Atrial Amplitude",
                                    command=lambda: self.changeAtrialAmp(self.atrialAmpEntry.get(), self.changeParamMessageBox))
        self.atrialAmpLabel.grid(row=5,column=0)
        self.atrialAmpEntry.grid(row=5, column=1)
        self.changeAtrialAmp.grid(row=5,column=2)
        
        #upperRateLimit
        self.URLLabel = tk.Label(self.parametersFrame,text=" Upper Rate limit: ")
        self.URLEntry = tk.Entry(self.parametersFrame)
        self.changeURL = tk.Button(self.parametersFrame, text="Change the URL(upper rate width)",
                                    command=lambda: self.changeURL(self.URLEntry.get(), self.changeParamMessageBox))
        self.URLLabel.grid(row=6,column=0)
        self.URLEntry.grid(row=6, column=1)
        self.changeURL.grid(row=6,column=2)

        #lower rate limit
        self.LRLLabel = tk.Label(self.parametersFrame,text="Lower Rate limit: ")
        self.LRLEntry = tk.Entry(self.parametersFrame)
        self.changeLRL = tk.Button(self.parametersFrame, text="Change LRL(Lower rate limit)",
                                    command=lambda: self.changeLRL(self.LRLEntry.get(), self.changeParamMessageBox))
        self.LRLLabel.grid(row=7,column=0)
        self.LRLEntry.grid(row=7, column=1)
        self.changeLRL.grid(row=7,column=2)
        
        #hysteresisRateLimit
        self.HRLLabel = tk.Label(self.parametersFrame,text="Hysteresis Rate Limit ")
        self.HRLEntry = tk.Entry(self.parametersFrame)
        self.changeHRL = tk.Button(self.parametersFrame, text="Change Hysteresis Rate Limit",
                                    command=lambda: self.changeHRL(self.HRLEntry.get(), self.changeParamMessageBox))
        self.HRLLabel.grid(row=8,column=0)
        self.HRLEntry.grid(row=8, column=1)
        self.changeHRL.grid(row=8,column=2)
        
        #ARP
        self.ARPLabel = tk.Label(self.parametersFrame,text="ARP")
        self.ARPEntry = tk.Entry(self.parametersFrame)
        self.changeARP = tk.Button(self.parametersFrame, text="Change ARP",
                                    command=lambda: self.changeARP(self.ARPEntry.get(), self.changeParamMessageBox))
        self.ARPLabel.grid(row=9,column=0)
        self.ARPEntry.grid(row=9, column=1)
        self.changeARP.grid(row=9,column=2)
        
        #VRP
        self.VRPLabel = tk.Label(self.parametersFrame,text="VRP")
        self.VRPEntry = tk.Entry(self.parametersFrame)
        self.changeVRP = tk.Button(self.parametersFrame, text="Change VRP",
                                    command=lambda: self.changeVRP(self.VRPEntry.get(), self.changeParamMessageBox))
        self.VRPLabel.grid(row=10,column=0)
        self.VRPEntry.grid(row=10, column=1)
        self.changeVRP.grid(row=10,column=2)
        
        #PVARP
        self.PVARPLabel = tk.Label(self.parametersFrame,text="PVARP:")
        self.PVARPEntry = tk.Entry(self.parametersFrame)
        self.changePVARP = tk.Button(self.parametersFrame, text="Change PVARP",
                                    command=lambda: self.changePVARP(self.PVARPEntry.get(), self.changeParamMessageBox))
        self.PVARPLabel.grid(row=11,column=0)
        self.PVARPEntry.grid(row=11, column=1)
        self.changePVARP.grid(row=11,column=2)
        
        
        

        #TODO add labels for all necessary user info ie:
        # self.heartRateLabel = tk.Label(self, text = "fjenfeuief")...
        self.parametersFrame.pack(side="top")
        
        self.user=None

        back_button = tk.Button(
            self,
            text="Back",
            command=lambda: self.backButtonCommand()
        )
        back_button.pack(side="top", anchor="nw")

    def backButtonCommand(self):
        self.lower()
        self.user = None
        
        ## change pacerate Button
    def changePaceRate(self, rate, message_box):
        if (self.user.setPacingRate(rate)):
            message_box.config(text="set pacing rate")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid pacing rate")
        ## MODE CHANGE Button 
    def changemode(self, mode, message_box):
        if (self.user.setMode(mode)):
            message_box.config(text="set Mode")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid Mode")
        ## change ventPW BUTTON
    def changeventPW(self, ventPW, message_box):
        if (self.user.setPacingRate(ventPW)):
            message_box.config(text="set ventricular pulse width")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid ventricular pulse width")
        
        ## change ventAmp BUTTON
    def changeventAmp(self, ventAmp, message_box):
        if (self.user.setventAmp(ventAmp)):
            message_box.config(text="set ventAmp")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid ventAmp")
            
        ## Change atrial pulse width button
    def changeatrialPW(self, atrialPW, message_box):
        if (self.user.setatrialPW(atrialPW)):
            message_box.config(text="set atrialPW")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid atrialPW")
        
        #upperRateLimit
    def changemode(self, URL, message_box):
        if (self.user.setURL(URL)):
            message_box.config(text="set upperRateLimit")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid upperRateLimit")
            
        
        # Lower Rate Limit
    def changemode(self, LRL, message_box):
        if (self.user.setLRL(LRL)):
            message_box.config(text="set Lower Rate Limit")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid Mode")
            
            
    #hysteresisRateLimit
    def changemode(self, HRL, message_box):
        if (self.user.setLRL(HRL)):
            message_box.config(text="set hysteresisRateLimit")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid hysteresisRateLimit")
    

    def changeARP(self, ARP, message_box):
        if (self.user.setARP(ARP)):
            message_box.config(text="set ARP")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid ARP")
        
        
        
        
    def set_user(self,user: UserClass):
        self.user = user

    def load_user_info(self):
        if not self.user: 
            return
        
        self.nameLabel.config(text = "Current user: {}".format(self.user.getUsername()))
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
        


        


    