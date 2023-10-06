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
            self.mode = f.readline().rstrip()

            self.ventPulseWidth = f.readline().rstrip()
            self.ventAmplitude = f.readline().rstrip()  
            self.atrialPulseWidth = f.readline().rstrip()  
            self.atrialAmplitude = f.readline().rstrip()  
            self.upperRateLimit = f.readline().rstrip()  
            self.lowerRateLimit = f.readline().rstrip()  

            self.ARP = f.readline().rstrip()  
            self.VRP = f.readline().rstrip()  
            self.PVARP = f.readline().rstrip()  
            self.hysteresisRateLimit = f.readline().rstrip()  


            


        except:
            self.file_found = False
            return
        
    def getUsername(self):
        return self.username
    

    #TODO make sure only allowed values are set 
    #  
    def setMode(self, mode: int):
        self.mode = mode

    def setVentPulseWidth(self, width: float):
        self.ventPulseWidth = width

    def setVentAmplitude(self, amp: float):
        self.ventAmplitude = amp

    def setAtrialPulseWidth(self, width: float):
        self.atrialPulseWidth = width

    def setAtrialAmplitude(self, amp: float):
        self.atrialAmplitude = amp

    def setUpperRateLimit(self, upper: int):
        self.upperRateLimit = upper

    def setLowerRateLimit(self, lower: int):
        self.upperRateLimit = lower

    def setARP(self, val: bool):
        self.ARP = val

    def setVRP(self, val: bool):
        self.VRP = val

    def setPVARP(self, val: bool):
        self.PVARP = val

    def setHysteresisRateLimit(self, limit: int):
        self.hysteresisRateLimit = limit