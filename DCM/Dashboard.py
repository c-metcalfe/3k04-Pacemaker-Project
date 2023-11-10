import tkinter as tk
from User import UserClass

class DashboardClass(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        back_button = tk.Button(self,text="Log out", command=lambda: self.backButtonCommand())
        back_button.pack(side="left", anchor="nw")
        
        go_to_graph_button = tk.Button(self, text="View Electrocardiogram Data", command = lambda: self.graphbuttoncommand())
        go_to_graph_button.pack(side="top", anchor = "s", padx=10)
        
        self.nameLabel = tk.Label(self, text="Dashboard")
        self.nameLabel.pack(padx=10, pady=10)
        
        self.parametersFrame = tk.LabelFrame(self, text="Parameters Dashboard")
        self.serialControlFrame = tk.LabelFrame(self, text="Serial Dashboard")

        self.connectionStatusLabel = tk.Label(self.serialControlFrame, text="Not Connected",fg="black", bg="red")
        self.connectionStatusLabel.pack(side="top")
        sendToPacemakerBtn = tk.Button(self.serialControlFrame, text="Send parameters to pacemaker", 
                                       command = lambda: print("this would send parameters to pacemaker"))
        
        self.serialMsgBox = tk.Label(self.serialControlFrame, text="No Serial communication yet").pack(side="top")
        sendToPacemakerBtn.pack(side="top", pady=10)


        self.changeParamMessageBox = tk.Label(self,font=('bold'),text="Enter values then use button to change indicated parameters")

        #headers
        labelHeader = tk.Label(self.parametersFrame, text="Parameter",font=("Comic Sans MS", 15, "bold"))
        entryHeader = tk.Label(self.parametersFrame, text="Entry",font=("Comic Sans MS", 15, "bold"))
        conditionHeader = tk.Label(self.parametersFrame, text="Conditions for Entry",font=("Comic Sans MS", 15, "bold"))

        labelHeader.grid(row=0,column=0)
        entryHeader.grid(row=0,column=1)
        conditionHeader.grid(row=0,column=3)
       
        # Creating instances of all table entries. Not all will be shown but all must be created so
        # their text can be modified.
        self.addPacingRateToTable(0)
        self.addModeToTable(1)
        self.addVentPWToTable(2)
        self.addVentAmpToTable(3)
        self.addAtrialPWToTable(4)
        self.addAtrialAmpToTable(5)
        self.addURLToTable(6)
        self.addLRLToTable(7)
        self.addHRLToTable(8)
        self.addARPToTable(9)
        self.addVRPToTable(10)
        self.addPVARPToTable(11)

        self.addSensitivityToTable(12)
        self.addActivityThresholdToTable(13)
        self.addReactionTimeToTable(14)
        self.addResponseFactorToTable(15)
        self.addRecoveryTimeToTable(16)
        self.addMaxSenseRateToTable(17)
            
        
        self.parametersFrame.pack(side="top")

        self.changeParamMessageBox.pack(side="top",pady=20)
        self.serialControlFrame.pack(side="top",pady=10)
        
        
        
        self.user=None # since their is no user, we have to wait until user logs in to set default mode

        

    def backButtonCommand(self):
        self.user = None
        self.controller.show_login()
        
    def graphbuttoncommand(self):
        self.user = None
        self.controller.show_egram()

           ## MODE CHANGE Button 
            ## TODO remove whole table, add table entries for each relevant parameter



    
    def changeMode(self, mode, message_box):
        if (self.user.setMode(mode)):
            message_box.config(text="Set Mode",fg="black")
            

            self.emptyTable()
            if(self.user.mode == 1): # AOO
                self.addModeToTable(0)
                self.addPacingRateToTable(1)
                self.addAtrialPWToTable(2)
                self.addAtrialAmpToTable(3)
                self.addURLToTable(4)
                self.addLRLToTable(5)

                self.load_user_info()
                

            elif(self.user.mode == 2): #VOO
                self.addModeToTable(0)
                self.addPacingRateToTable(1)
                self.addVentPWToTable(2)
                self.addVentAmpToTable(3)
                self.addURLToTable(4)
                self.addLRLToTable(5)

                self.load_user_info()
                

            elif(self.user.mode == 3): #AAI
                self.addModeToTable(0)
                self.addPacingRateToTable(1)
                self.addAtrialPWToTable(2)
                self.addAtrialAmpToTable(3)
                self.addURLToTable(4)
                self.addLRLToTable(5)
                self.addARPToTable(6)

                self.load_user_info()

            elif(self.user.mode == 4): #VVI
                self.addModeToTable(0)
                self.addPacingRateToTable(1)
                self.addVentPWToTable(2)
                self.addVentAmpToTable(3)
                self.addURLToTable(4)
                self.addLRLToTable(5)
                self.addVRPToTable(6)

                self.load_user_info()               
                                
            elif(self.user.mode == 5): #AOOR
                self.addModeToTable(0)
                self.addPacingRateToTable(1)
                self.addAtrialPWToTable(2)
                self.addAtrialAmpToTable(3)
                self.addURLToTable(4)
                self.addLRLToTable(5)
                self.addActivityThresholdToTable(6)
                self.addReactionTimeToTable(7)
                self.addResponseFactorToTable(8)
                self.addRecoveryTimeToTable(9)
                self.addMaxSenseRateToTable(10)

                self.load_user_info()
                
            elif(self.user.mode == 6): #VOOR
                self.addModeToTable(0)
                self.addPacingRateToTable(1)
                self.addVentPWToTable(2)
                self.addVentAmpToTable(3)
                self.addURLToTable(4)
                self.addLRLToTable(5)
                self.addActivityThresholdToTable(6)
                self.addReactionTimeToTable(7)
                self.addResponseFactorToTable(8)
                self.addRecoveryTimeToTable(9)
                self.addMaxSenseRateToTable(10)

                self.load_user_info()
        
            elif(self.user.mode == 7): #AAIR
                self.addModeToTable(0)
                self.addPacingRateToTable(1)
                self.addAtrialPWToTable(2)
                self.addAtrialAmpToTable(3)
                self.addURLToTable(4)
                self.addLRLToTable(5)
                self.addARPToTable(6)

                self.addActivityThresholdToTable(7)
                self.addReactionTimeToTable(8)
                self.addResponseFactorToTable(9)
                self.addRecoveryTimeToTable(10)
                self.addMaxSenseRateToTable(11)

                self.load_user_info()
        
            elif(self.user.mode == 8): #VVIR
                self.addModeToTable(0)
                self.addPacingRateToTable(1)
                self.addVentPWToTable(2)
                self.addVentAmpToTable(3)
                self.addURLToTable(4)
                self.addLRLToTable(5)
                self.addVRPToTable(6)

                self.addActivityThresholdToTable(7)
                self.addReactionTimeToTable(8)
                self.addResponseFactorToTable(9)
                self.addRecoveryTimeToTable(10)
                self.addMaxSenseRateToTable(11)

                self.load_user_info()

            else:  # Should never happen
                self.load_user_info()
                print("ERROR UINDUIFENFHUIFH")
        else:
            message_box.config(text="Error: invalid Mode",fg="red")
                

    
    def emptyTable(self):
        for widget in self.parametersFrame.winfo_children():
            widget.grid_remove()


    def addPacingRateToTable(self, currentNumRows):
        row1 =currentNumRows+1
        self.rateLabel = tk.Label(self.parametersFrame,text="Pacing Rate:")
        rateLabel2 = tk.Label(self.parametersFrame,text="Must be an integer between lower and upper rate limits.")
        rateEntry = tk.Entry(self.parametersFrame)
        changeRateBtn = tk.Button(self.parametersFrame, text="Change rate", 
                                    command=lambda: self.changePaceRate(rateEntry.get(), self.changeParamMessageBox))
        self.rateLabel.grid(row=row1,column=0)
        rateEntry.grid(row=row1, column=1)
        changeRateBtn.grid(row=row1,column=2,sticky="W")
        rateLabel2.grid(row=row1,column=3,sticky="W")

    def addModeToTable(self, currentNumRows):
        row1 =currentNumRows+1
        self.modeLabel = tk.Label(self.parametersFrame,text=" Pacing Mode:")
        modeLabel2 = tk.Label(self.parametersFrame, wraplength=400, text="Must me a valid Mode name (AOO, VOO, AII, VII, AOOR, VOOR, AAIR, VIIR) or mode number (1-8)")
        modeEntry = tk.Entry(self.parametersFrame)
        changeModeBtn = tk.Button(self.parametersFrame, text="Change Mode",
                                  command=lambda: self.changeMode(modeEntry.get(), self.changeParamMessageBox))
        self.modeLabel.grid(row=row1,column=0)
        modeEntry.grid(row=row1, column=1)
        changeModeBtn.grid(row=row1,column=2,sticky="W")
        modeLabel2.grid(row=row1,column=3,sticky="W")

    def addVentPWToTable(self, currentNumRows):
        row1=currentNumRows+1
        self.ventPWLabel = tk.Label(self.parametersFrame,text=" Ventricular Pulse Width: ")
        ventPWLabel2 = tk.Label(self.parametersFrame,text="Must be a number in the range [0.3, 1.9] with one decimal place")
        ventPWEntry = tk.Entry(self.parametersFrame)
        changeVentPWBtn = tk.Button(self.parametersFrame, text="Change Ventricular Pulse Width",
                                    command=lambda: self.changeVentPW(ventPWEntry.get(), self.changeParamMessageBox))
        self.ventPWLabel.grid(row=row1,column=0)
        ventPWEntry.grid(row=row1, column=1)
        changeVentPWBtn.grid(row=row1,column=2,sticky="W")
        ventPWLabel2.grid(row=row1,column=3,sticky="W")

    def addVentAmpToTable(self, currentNumRows):
        row1=currentNumRows+1
        self.ventAmpLabel = tk.Label(self.parametersFrame,text="Ventricular amplitude: ")
        ventAmpLabel2 = tk.Label(self.parametersFrame,text="Must be a number in the range [0, 5.0] with at most one decimal place")
        ventAmpEntry = tk.Entry(self.parametersFrame)
        changeVentAmpBtn = tk.Button(self.parametersFrame, text="Change VA",
                                    command=lambda: self.changeVentAmp(ventAmpEntry.get(), self.changeParamMessageBox))
        self.ventAmpLabel.grid(row=row1,column=0)
        ventAmpEntry.grid(row=row1, column=1)
        changeVentAmpBtn.grid(row=row1,column=2,sticky="W")
        ventAmpLabel2.grid(row=row1,column=3,sticky="W")

    def addAtrialPWToTable(self, currentNumRows):
        row1=currentNumRows+1
        
        self.atrialPWLabel = tk.Label(self.parametersFrame,text=" Atrial Pulse Width: ")
        atrialPWLabel2 = tk.Label(self.parametersFrame,text="Must be an integer in the range [1, 30]")
        atrialPWEntry = tk.Entry(self.parametersFrame)
        changeAtrialPWBtn = tk.Button(self.parametersFrame, text="Change Atrial Pulse Width",
                                    command=lambda: self.changeAtrialPW(atrialPWEntry.get(), self.changeParamMessageBox))
        self.atrialPWLabel.grid(row=row1,column=0)
        atrialPWEntry.grid(row=row1, column=1)
        changeAtrialPWBtn.grid(row=row1,column=2,sticky="W")
        atrialPWLabel2.grid(row=row1,column=3,sticky="W")

    def addAtrialAmpToTable(self, currentNumRows):
        row1=currentNumRows+1
        self.atrialAmpLabel = tk.Label(self.parametersFrame,text=" Atrial Amplitude: ")
        atrialAmpLabel2 = tk.Label(self.parametersFrame,text="Must be a number in the range [0, 5.0] with at most one decimal place")
        atrialAmpEntry = tk.Entry(self.parametersFrame)
        changeAtrialAmpBtn = tk.Button(self.parametersFrame, text="Change Atrial Amplitude",
                                    command=lambda: self.changeAtrialAmp(atrialAmpEntry.get(), self.changeParamMessageBox))
        self.atrialAmpLabel.grid(row=row1,column=0)
        atrialAmpEntry.grid(row=row1, column=1)
        changeAtrialAmpBtn.grid(row=row1,column=2,sticky="W")
        atrialAmpLabel2.grid(row=row1,column=3,sticky="W")

    def addURLToTable(self, currentNumRows):
        row1=currentNumRows+1
        self.URLLabel = tk.Label(self.parametersFrame,text=" Upper Rate limit: ")
        URLLabel2 = tk.Label(self.parametersFrame,wraplength="400", justify="left",
                             text="Must be an interger in the range [50,175] that is divisible by 5 and greater than the current pacing rate")
        URLEntry = tk.Entry(self.parametersFrame)
        changeURLBtn = tk.Button(self.parametersFrame, text="Change the URL(upper rate width)",
                                    command=lambda: self.changeURL(URLEntry.get(), self.changeParamMessageBox))
        self.URLLabel.grid(row=row1,column=0)
        URLEntry.grid(row=row1, column=1)
        changeURLBtn.grid(row=row1,column=2,sticky="W")
        URLLabel2.grid(row=row1,column=3,sticky="W")

    def addLRLToTable(self, currentNumRows):
        row1=currentNumRows+1
        self.LRLLabel = tk.Label(self.parametersFrame,text="Lower Rate limit: ")
        LRLLabel2 = tk.Label(self.parametersFrame,wraplength="400", justify="left",
                             text="Must be an integer in the range [30,175] that is divisible by 5, less than the upper rate limit, and less than the current pacing rate")
        LRLEntry = tk.Entry(self.parametersFrame)
        changeLRLBtn = tk.Button(self.parametersFrame, text="Change LRL(Lower rate limit)",
                                    command=lambda: self.changeLRL(LRLEntry.get(), self.changeParamMessageBox))
        self.LRLLabel.grid(row=row1,column=0)
        LRLEntry.grid(row=row1, column=1)
        changeLRLBtn.grid(row=row1,column=2,sticky="W")
        LRLLabel2.grid(row=row1,column=3,sticky="W")

    def addHRLToTable(self, currentNumRows):
        row1=currentNumRows+1
        self.HRLLabel = tk.Label(self.parametersFrame,text= " Hysteresis Rate Limit ")
        HRLLabel2 = tk.Label(self.parametersFrame,wraplength="400", justify="left",
                             text="Must be 0 or an integer in the range [30,175] that is divisible by 5 and less than the upper rate limit")
        HRLEntry = tk.Entry(self.parametersFrame)
        changeHRLBtn = tk.Button(self.parametersFrame, text="Change Hysteresis Rate Limit",
                                    command=lambda: self.changeHRL(HRLEntry.get(), self.changeParamMessageBox))
        self.HRLLabel.grid(row=row1,column=0)
        HRLEntry.grid(row=row1, column=1)
        changeHRLBtn.grid(row=row1,column=2,sticky="W")
        HRLLabel2.grid(row=row1,column=3,sticky="W")

    def addARPToTable(self, currentNumRows):
        row1=currentNumRows+1  
        self.ARPLabel = tk.Label(self.parametersFrame,text="ARP")
        ARPLabel2 = tk.Label(self.parametersFrame,wraplength="400",text="Must be an integer in the range [150, 500] that is divisible by 10")
        ARPEntry = tk.Entry(self.parametersFrame)
        changeARPBtn = tk.Button(self.parametersFrame, text="Change ARP",
                               command=lambda: self.changeARP(ARPEntry.get(), self.changeParamMessageBox))
        self.ARPLabel.grid(row=row1,column=0)
        ARPEntry.grid(row=row1, column=1)
        changeARPBtn.grid(row=row1,column=2,sticky="W")
        ARPLabel2.grid(row=row1,column=3,sticky="W")

    def addVRPToTable(self, currentNumRows):
        row1=currentNumRows+1  
        self.VRPLabel = tk.Label(self.parametersFrame,text="VRP")
        VRPLabel2= tk.Label(self.parametersFrame,wraplength="400",text="Must be an integer in the range [150, 500] that is divisible by 10")
        VRPEntry = tk.Entry(self.parametersFrame)
        changeVRPBtn = tk.Button(self.parametersFrame, text="Change VRP",
                               command=lambda: self.changeVRP(VRPEntry.get(), self.changeParamMessageBox))
        self.VRPLabel.grid(row=row1,column=0)
        VRPEntry.grid(row=row1, column=1)
        changeVRPBtn.grid(row=row1,column=2,sticky="W")
        VRPLabel2.grid(row=row1,column=3,sticky="W")

    def addPVARPToTable(self, currentNumRows):
        row1=currentNumRows+1  
        self.PVARPLabel = tk.Label(self.parametersFrame,text="PVARP:")
        PVARPLabel2= tk.Label(self.parametersFrame,wraplength="400",text="Must be an integer in the range [150, 500] that is divisible by 10")
        PVARPEntry = tk.Entry(self.parametersFrame)
        changePVARPBtn = tk.Button(self.parametersFrame, text="Change PVARP",
                               command=lambda: self.changePVARP(PVARPEntry.get(), self.changeParamMessageBox))
        self.PVARPLabel.grid(row=row1,column=0)
        PVARPEntry.grid(row=row1, column=1)
        changePVARPBtn.grid(row=row1,column=2,sticky="W")
        PVARPLabel2.grid(row=row1,column=3,sticky="W")

    def addSensitivityToTable(self, currentNumRows):
        row1=currentNumRows+1  
        self.SensitivityLabel = tk.Label(self.parametersFrame,text= "Sensitivity:")
        SensitivityLabel2= tk.Label(self.parametersFrame,wraplength="400",text="Allowed values are: 0.25, 0.5, 0.75, 1, 1.5, 2,, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5 10")
        SensitivityEntry = tk.Entry(self.parametersFrame)
        changeSensitivityBtn = tk.Button(self.parametersFrame, text="Change Sensitivity",
                               command=lambda: self.changeSensitivity(SensitivityEntry.get(), self.changeParamMessageBox))
        self.PVARPLabel.grid(row=row1,column=0)
        SensitivityEntry.grid(row=row1, column=1)
        changeSensitivityBtn.grid(row=row1,column=2,sticky="W")
        SensitivityLabel2.grid(row=row1,column=3,sticky="W")

    def addActivityThresholdToTable(self, currentNumRows):
        row1=currentNumRows+1  
        self.ActivityThresholdLabel = tk.Label(self.parametersFrame,text="Activity Threshold:")
        ActivityThresholdLabel2= tk.Label(self.parametersFrame,wraplength="400",text="Allowed values are: V-Low, Low, Med-Low, Med, Med-High, High, V-High, or the number from 0-6 corresponding to each option.")
        ActivityThresholdEntry = tk.Entry(self.parametersFrame)
        changeActivityThresholdBtn = tk.Button(self.parametersFrame, text="Change Activity Threshold",
                               command=lambda: self.changeActivityThreshold(ActivityThresholdEntry.get(), self.changeParamMessageBox))
        self.ActivityThresholdLabel.grid(row=row1,column=0)
        ActivityThresholdEntry.grid(row=row1, column=1)
        changeActivityThresholdBtn.grid(row=row1,column=2,sticky="W")
        ActivityThresholdLabel2.grid(row=row1,column=3,sticky="W")

    def addReactionTimeToTable(self, currentNumRows):
        row1=currentNumRows+1  
        self.ReactionTimeLabel = tk.Label(self.parametersFrame,text="Reaction Time:")
        ReactionTimeLabel2= tk.Label(self.parametersFrame,wraplength="400",text="Must be a number in [10,50] that is divisible by 10")
        ReactionTimeEntry = tk.Entry(self.parametersFrame)
        changeReactionTimeBtn = tk.Button(self.parametersFrame, text="Change Reaction Time",
                               command=lambda: self.changeReactionTime(ReactionTimeEntry.get(), self.changeParamMessageBox))
        self.ReactionTimeLabel.grid(row=row1,column=0)
        ReactionTimeEntry.grid(row=row1, column=1)
        changeReactionTimeBtn.grid(row=row1,column=2,sticky="W")
        ReactionTimeLabel2.grid(row=row1,column=3,sticky="W")

    def addResponseFactorToTable(self, currentNumRows):
        row1=currentNumRows+1  
        self.ResponseFactorLabel = tk.Label(self.parametersFrame,text="Response Factor:")
        ResponseFactorLabel2= tk.Label(self.parametersFrame,wraplength="400",text="Must be an integer in [1, 16]")
        ResponseFactorEntry = tk.Entry(self.parametersFrame)
        changeResponseFactorBtn = tk.Button(self.parametersFrame, text="Change Reaction Time",
                               command=lambda: self.changeResponseFactor(ResponseFactorEntry.get(), self.changeParamMessageBox))
        self.ResponseFactorLabel.grid(row=row1,column=0)
        ResponseFactorEntry.grid(row=row1, column=1)
        changeResponseFactorBtn.grid(row=row1,column=2,sticky="W")
        ResponseFactorLabel2.grid(row=row1,column=3,sticky="W")

        # TODO keep adding table things

    

    def addRecoveryTimeToTable(self, currentNumRows):
        row1=currentNumRows+1  
        self.RecoveryTimeLabel = tk.Label(self.parametersFrame,text= "Recovery Time:")
        RecoveryTimeLabel2= tk.Label(self.parametersFrame,wraplength="400",text=" Must be an integer in [2, 16]")
        RecoveryTimeEntry = tk.Entry(self.parametersFrame)
        changeRecoveryTimeBtn = tk.Button(self.parametersFrame, text="Change Recovery Time",
                               command=lambda: self.changeRecoveryTime(RecoveryTimeEntry.get(), self.changeParamMessageBox))
        self.RecoveryTimeLabel.grid(row=row1,column=0)
        RecoveryTimeEntry.grid(row=row1, column=1)
        changeRecoveryTimeBtn.grid(row=row1,column=2,sticky="W")
        RecoveryTimeLabel2.grid(row=row1,column=3,sticky="W")

    def addMaxSenseRateToTable(self, currentNumRows):
        row1=currentNumRows+1  
        self.MaxSenseRateLabel = tk.Label(self.parametersFrame,text= "Max Sensor Rate:")
        MaxSenseRateLabel2= tk.Label(self.parametersFrame,wraplength="400",text="Must be an integer in [50, 175] that is divisible by 5")
        MaxSenseRateEntry = tk.Entry(self.parametersFrame)
        changeMaxSenseRateBtn = tk.Button(self.parametersFrame, text="Change Recovery Time",
                               command=lambda: self.changeMaxSenseRate(MaxSenseRateEntry.get(), self.changeParamMessageBox))
        self.MaxSenseRateLabel.grid(row=row1,column=0)
        MaxSenseRateEntry.grid(row=row1, column=1)
        changeMaxSenseRateBtn.grid(row=row1,column=2,sticky="W")
        MaxSenseRateLabel2.grid(row=row1,column=3,sticky="W")




        ## change pacerate Button
    def changePaceRate(self, rate, message_box):
        if (self.user.setPacingRate(rate)):
            message_box.config(text="Set pacing rate",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid pacing rate",fg="red")
 
        ## change ventPW BUTTON
    def changeVentPW(self, ventPW, message_box):
        if (self.user.setVentPulseWidth(ventPW)):
            message_box.config(text="Set ventricular pulse width",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid ventricular pulse width",fg="red")
        
        ## change ventAmp BUTTON
    def changeVentAmp(self, ventAmp, message_box):
        if (self.user.setVentAmplitude(ventAmp)):
            message_box.config(text="Set ventAmp",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid ventAmp",fg="red")
            
        ## Change atrial pulse width button
    def changeAtrialPW(self, atrialPW, message_box):
        if (self.user.setAtrialPulseWidth(atrialPW)):
            message_box.config(text="Set Atrial Pulse Width",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid atrialPW",fg="red")
        
    #change atrial amp button
    def changeAtrialAmp(self, atrialAmp, message_box):
        if (self.user.setAtrialAmplitude(atrialAmp)):
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

    def changeSensitivity(self, sensitivity, message_box):
        if (self.user.setsensitivity_adjustment(sensitivity)):
            message_box.config(text="set sensitivity",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid sensitivity",fg="red")
    
    def changeActivityThreshold(self, ActivityThreshold, message_box):
        if (self.user.set_activity_threshold(ActivityThreshold)):
            message_box.config(text="set Activity Threshold",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid Activity Threshold",fg="red")

    def changeReactionTime(self, ReactionTime, message_box):
        if (self.user.setReactionTime(ReactionTime)):
            message_box.config(text="set Reaction Time",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid Reaction Time",fg="red")
            
    def changeResponseFactor(self, ResponseFactor, message_box):
        if (self.user.setResponseFactor(ResponseFactor)):
            message_box.config(text="set Response Factor",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid Response Factor",fg="red")

    def changeRecoveryTime(self, RecoveryTime, message_box):
        if (self.user.setRecoveryTime(RecoveryTime)):
            message_box.config(text="set Recovery Time",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid Recovery Time",fg="red")
    
    def changeMaxSenseRate(self, MaxSenseRate, message_box):
        if (self.user.setMaxSenseRate(MaxSenseRate)):
            message_box.config(text="set Max Sensor Rate",fg="black")
            self.load_user_info()
        else:
            message_box.config(text="Error: invalid Max Sensor Rate",fg="red")

    def set_user(self,user: UserClass):
        self.user = user

    def load_user_info(self):
        if not self.user: 
            return
        
        self.nameLabel.config(text = "Current user: {}".format(self.user.getUsername()), font = ("Arial Baltic", 30, "bold"))
        self.nameLabel.pack(pady = 25)
        self.rateLabel.config(text = "Pacing Rate: {}".format(self.user.pacingRate))

        mode = self.user.mode
        if mode == 1: modeText = "AOO"
        elif mode == 2: modeText = "VOO"
        elif mode == 3: modeText = "AAI"
        elif mode == 4: modeText = "VVI"
        elif mode == 5: modeText = "AOOR"
        elif mode == 6: modeText = "VOOR"
        elif mode == 7: modeText = "AAIR"
        elif mode == 8: modeText = "VVIR"        
        else: modeText = "ERROR"
        self.modeLabel.config(text = "Mode: {}".format(modeText))

        
        self.ventPWLabel.config(text="Ventricular Pulse Width (ms): {}".format(self.user.ventPulseWidth))
        self.ventAmpLabel.config(text="Ventricular Amplitude (V): {}".format(self.user.ventAmplitude))
        self.atrialPWLabel.config(text="Atrial Pulse Width (ms): {}".format(self.user.atrialPulseWidth))
        self.atrialAmpLabel.config(text="Atrial Amplitude (V): {}".format(self.user.atrialAmplitude))
        self.URLLabel.config(text="Upper Rate Limit (ppm): {}".format(self.user.upperRateLimit))
        self.LRLLabel.config(text="Lower Rate Limit (ppm): {}".format(self.user.lowerRateLimit))
        self.HRLLabel.config(text="Hysteresis Rate Limit (ppm): {}".format(self.user.hysteresisRateLimit))
        self.ARPLabel.config(text="Atrial Refractory Period (ms): {}".format(self.user.ARP))
        self.VRPLabel.config(text="Ventricular Refractory Period (ms): {}".format(self.user.VRP))
        self.PVARPLabel.config(text="Post-Ventricular Atrial Refractory Period (ms): {}".format(self.user.ARP))
        self.SensitivityLabel.config(text="Sensitivity (mV): {}".format(self.user.sensitivity))
        self.ReactionTimeLabel.config(text="Reaction Time (s): {}".format(self.user.reactionTime))
        self.ResponseFactorLabel.config(text="Response Factor: {}".format(self.user.responseFactor))
        self.RecoveryTimeLabel.config(text="Recovery Time (min): {}".format(self.user.recoveryTime))
        self.MaxSenseRateLabel.config(text="Maximum Sensor Rate (ppm): {}".format(self.user.maxSensorRate))

        if self.user.activityThreshold == 0: aTText = "V-Low"
        elif self.user.activityThreshold == 1: aTText = "Low"
        elif self.user.activityThreshold == 2: aTText = "Med-Low"
        elif self.user.activityThreshold == 3: aTText = "Med"
        elif self.user.activityThreshold == 4: aTText = "Med-High"
        elif self.user.activityThreshold == 5: aTText = "High"
        elif self.user.activityThreshold == 6: aTText = "V-High"

        self.ActivityThresholdLabel.config(text="Activity Threshold: {}".format(aTText))



        #self.changeParamMessageBox.config(text="Enter values then use button to change indicated parameters")
        


        


    