import os

class UserClass:
    def __init__(self, username): # This is not the function that creates a new user, see RegisterPage.py
        # open file from Users folder named "username"
        # assign parameter values from file
        # maybe encrypt file?
        try:
            file_name = os.path.join("DCM","Users", username, "{}.txt".format(username))
            f = open(file_name)
            self.file_found = True
            self.username = f.readline().rstrip()  # remove newlines from username and pw with rstrip
            
            self.password = f.readline().rstrip() 

            # read pacemaker parameters to user attributes 
            self.pacingRate = int(f.readline().rstrip())
            self.mode = int(f.readline().rstrip())
            self.ventPulseWidth = float(f.readline().rstrip())
            self.ventAmplitude = float(f.readline().rstrip())
            self.atrialPulseWidth = float(f.readline().rstrip())
            self.atrialAmplitude = float(f.readline().rstrip())  
            self.upperRateLimit = int(f.readline().rstrip())  
            self.lowerRateLimit = int(f.readline().rstrip()) 

            self.ARP = int(f.readline().rstrip())  
            self.VRP = int(f.readline().rstrip())  
            self.PVARP = int(f.readline().rstrip())
            self.hysteresisRateLimit = int(f.readline().rstrip())
            
            # self.activityThreshold = (f.readline().rstrip())  # TODO STRING?
            # self.reactionTime  = int(f.readline().rstrip())
            # self.responseFactor  = int(f.readline().rstrip())
            # self.recoveryTime = int(f.readline().rstrip())


        except:
            self.file_found = False
            return
        
    def getUsername(self):
        return self.username
    
    def overwriteUserData(self)->bool:
        filename = "{}.txt".format(self.username)
        file_path = os.path.join("DCM","Users",self.username,filename)

        try:
            user_file = open(file_path,"w")  
        
            user_file.write("{}\n".format(self.username))  
            user_file.write("{}\n".format(self.password)) 
            user_file.write("{}\n".format(self.pacingRate)) 
            user_file.write("{}\n".format(self.mode))  
            user_file.write("{}\n".format(self.ventPulseWidth))  
            user_file.write("{}\n".format(self.ventAmplitude))  
            user_file.write("{}\n".format(self.atrialPulseWidth))  
            user_file.write("{}\n".format(self.atrialAmplitude))  
            user_file.write("{}\n".format(self.upperRateLimit))  
            user_file.write("{}\n".format(self.lowerRateLimit))  
            user_file.write("{}\n".format(self.ARP))  
            user_file.write("{}\n".format(self.VRP))  
            user_file.write("{}\n".format(self.PVARP))  
            user_file.write("{}\n".format(self.hysteresisRateLimit)) 
            # user_file.write("{}\n".format(self.activityThreshold))  
            # user_file.write("{}\n".format(self.reactionTime))  
            # user_file.write("{}\n".format(self.responseFactor))  
            # user_file.write("{}\n".format(self.recoveryTime)) 

            user_file.close()
            return True
        except:
            return False

        
    

    #TODO add set functions for 4 new params
    #  
    def setPacingRate(self, rate)->bool:
        try:
            rateInt = int(rate)
        except:
            return False
        if (self.lowerRateLimit <= rateInt and self.upperRateLimit>=rateInt):
            self.pacingRate = rateInt
            self.overwriteUserData()
            return True
        return False
  
    def setMode(self, mode)->bool:
        try:
            modeInt = int(mode)
            if(modeInt <9 and modeInt>0):
                self.mode = modeInt
                self.overwriteUserData()
                return True
        except:
            if(mode == "AOO"): 
                self.mode = 1
                self.overwriteUserData()
                return True
            elif(mode == "VOO"): 
                self.mode = 2
                self.overwriteUserData()
                return True
            elif(mode == "AAI"): 
                self.mode = 3
                self.overwriteUserData()
                return True
            elif(mode == "VVI"): 
                self.mode = 4
                self.overwriteUserData()
                return True
            elif(mode == "AOOR"): 
                self.mode = 5
                self.overwriteUserData()
                return True
            elif(mode == "VOOR"): 
                self.mode = 6
                self.overwriteUserData()
                return True
            elif(mode == "AAIR"): 
                self.mode = 7
                self.overwriteUserData()
                return True
            elif(mode == "VVIR"): 
                self.mode = 8
                self.overwriteUserData()
                return True                                   
            else:
                return False

    def setVentPulseWidth(self, width)->bool:
        try:
            widthFloat = float(width)
        except:
            return False
        allowed_vals = [0.3,0.4,0.5,0.6,0.7,
                        0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,
                        1.7,1.8,1.9]
        if (widthFloat in allowed_vals):
            self.ventPulseWidth = widthFloat
            self.overwriteUserData()
            return True
        return False

    def setVentAmplitude(self, amp)->bool:
        try:
            ampFloat = float(amp)
        except:
            return False
        allowed_vals = [2.5,3.0,3.5,4.0,4.5,5.0]
        if (ampFloat in allowed_vals):
            self.ventAmplitude = ampFloat
            self.overwriteUserData()
            return True
        return False

    def setAtrialPulseWidth(self, width)->bool:
        try:
            widthFloat = float(width)
        except:
            return False
        allowed_vals = [0.3,0.4,0.5,0.6,0.7,
                        0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,
                        1.7,1.8,1.9]
        if (widthFloat in allowed_vals):
            self.atrialPulseWidth = widthFloat
            self.overwriteUserData()
            return True
        return False

    def setAtrialAmplitude(self, amp)->bool:
        try:
            ampFloat = float(amp)
        except:
            return False
        allowed_vals = [2.5,3.0,3.5,4.0,4.5,5.0]
        if (ampFloat in allowed_vals):
            self.atrialAmplitude = ampFloat
            self.overwriteUserData()
            return True
        return False

    def setUpperRateLimit(self, upper)->bool:
        try:
            upperInt = int(upper)
        except:
            return False
        if(upperInt>175 or upperInt <50 or upperInt<self.pacingRate):return False
        if(upperInt%5 != 0): return False
        self.upperRateLimit= upperInt
        self.overwriteUserData()
        return True
        

    def setLowerRateLimit(self, lower)->bool:
        try:
            lowerInt = int(lower)
        except:
            return False
        if(lowerInt>175 or lowerInt <30):return False
        if(lowerInt>self.pacingRate):return False
        if(lowerInt>self.upperRateLimit):return False
        if((lowerInt<=50 or lowerInt >=90) and lowerInt%5 != 0): return False
        self.lowerRateLimit= lowerInt
        self.overwriteUserData()
        return True

    def setARP(self, val)->bool:
        try:
            valInt = int(val)
        except:
            return False
        if(valInt%10 != 0): return False
        if(valInt<150 or valInt>500): return False
        self.ARP = valInt
        self.overwriteUserData()
        return True

    def setVRP(self, val)->bool:
        try:
            valInt = int(val)
        except:
            return False
        if(valInt%10 != 0): return False
        if(valInt<150 or valInt>500): return False
        self.ARP = valInt
        self.overwriteUserData()
        return True

    def setPVARP(self, val)->bool:
        try:
            valInt = int(val)
        except:
            return False
        if(valInt%10 != 0): return False
        if(valInt<150 or valInt>500): return False
        self.ARP = valInt
        self.overwriteUserData()
        return True

    def setHysteresisRateLimit(self, limit)->bool:
        try:
            limitInt = int(limit)
        except:
            return False
        
        if limitInt==0: 
            self.hysteresisRateLimit = limitInt
            self.overwriteUserData()
            return True
        if(limitInt>175 or limitInt <30):return False
        if((limitInt<=50 or limitInt >=90) and limitInt%5 != 0): return False
        self.hysteresisRateLimit= limitInt
        self.overwriteUserData()
        return True