import os

class UserClass:
    def __init__(self, user_file): # This is not the function that creates a new user, see RegisterPage.py
        # open file from Users folder named "username"
        # assign parameter values from file
        # maybe encrypt file?
        try:
            file_name = os.path.join("DCM","Users","{}.txt".format(user_file))
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

        except:
            self.file_found = False
            return
        
    def getUsername(self):
        return self.username
    
    def overwriteUserData(self)->bool:
        filename = "{}.txt".format(self.username)
        file_path = os.path.join("DCM","Users",filename)

        try:
            user_file = open(file_path,"w")  
        except:
            return False
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

        user_file.close()
        return True

        
    

    #TODO make sure only allowed values are set 
    #  
    def setPacingRate(self, rate: int)->bool:
        if type(rate) != int:
            return False
        if (self.lowerRateLimit <= rate and self.upperRateLimit>=rate):
            self.pacingRate = rate
            return True
        return False

    def setMode(self, mode: int)->bool:
        self.mode = mode

    def setVentPulseWidth(self, width: float)->bool:
        if type(width != float): return False
        allowed_vals = [0.3,0.4,0.5,0.6,0.7,
                        0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,
                        1.7,1.8,1.9]
        if (width in allowed_vals):
            self.ventPulseWidth = width
            return True
        return False

    def setVentAmplitude(self, amp: float)->bool:
        if type(amp != float): return False
        allowed_vals = [2.5,3.0,3.5,4.0,4.5,5.0]
        if (amp in allowed_vals):
            self.ventAmplitude = amp
            return True
        return False

    def setAtrialPulseWidth(self, width: float)->bool:
        if type(width != float): return False
        allowed_vals = [0.3,0.4,0.5,0.6,0.7,
                        0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,
                        1.7,1.8,1.9]
        if (width in allowed_vals):
            self.atrialPulseWidth = width
            return True
        return False

    def setAtrialAmplitude(self, amp: float)->bool:
        if type(amp != float): return False
        allowed_vals = [2.5,3.0,3.5,4.0,4.5,5.0]
        if (amp in allowed_vals):
            self.atrAmplitudeAmplitude = amp
            return True
        return False

    def setUpperRateLimit(self, upper: int)->bool:
        if(type(upper)!=int): return False
        if(upper>175 or upper <50):return False
        if(upper%5 != 0): return False
        self.upperRateLimit= upper
        return True
        

    def setLowerRateLimit(self, lower: int)->bool:
        if(type(lower)!=int): return False
        if(lower>175 or lower <30):return False
        if((lower<=50 or lower >=90) and lower%5 != 0): return False
        self.lowerRateLimit= lower
        return True

    def setARP(self, val: int)->bool:
        if(type(val) != int): return False
        if(val%10 != 0): return False
        if(val<150 or val>500): return False
        self.ARP = val
        return True

    def setVRP(self, val: int)->bool:
        if(type(val) != int): return False
        if(val%10 != 0): return False
        if(val<150 or val>500): return False
        self.VRP = val
        return True

    def setPVARP(self, val: int)->bool:
        if(type(val) != int): return False
        if(val%10 != 0): return False
        if(val<150 or val>500): return False
        self.PVARP = val
        return True

    def setHysteresisRateLimit(self, limit: int)->bool:
        if(type(limit)!=int): return False
        if limit==0: 
            self.hysteresisRateLimit = limit
            return True
        if(limit>175 or limit <30):return False
        if((limit<=50 or limit >=90) and limit%5 != 0): return False
        self.hysteresisRateLimit= limit
        return True