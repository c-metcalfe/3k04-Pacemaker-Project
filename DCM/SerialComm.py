import serial
import time
import User

class serialComm():
    def __init__(self, user: User):
        self.ser = serial.Serial()
        self.user = user
        self.ser.port = "COM5"  # device specific
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.baudrate = 9600
        self.ser.parity = serial.PARITY_EVEN
        self.ser.stopbits = 1
        self.ser.timeout = 2
        ### this is the port that it connects to on my laptop -colin

    def attempt_connect(self):
        try:
            self.ser.open()
        except:
            pass
        if not self.ser.is_open:
            print("Failed to open port")
            return False
        return True 
    
    def send_packet(self): # send packet to pacemaker in correct format 
        user = self.user
        paramsList = [user.mode,
                      user.lowerRateLimit,
                      user.upperRateLimit,
                      int(10*user.atrialAmplitude),
                      int(10*user.ventAmplitude), 
                      user.atrialPulseWidth, 
                      user.ventPulseWidth, 
                      int(user.VRP /10),
                      int(user.ARP /10), 
                      user.activityThreshold, 
                      user.reactionTime, 
                      user.responseFactor, 
                      user.recoveryTime,
                      0,
                      0,
                      0]# 0's are reserved
        binaryParams = bytearray(paramsList)
        # for param in paramsList:
        #     print(type(param), end=", ") 
        # print(paramsList)
        # print(binaryParams)
    
        #binaryParams.append(checksum(binaryParams))

        self.ser.write(binaryParams)

        

def checksum(binaryParams):
        sum = 0
        for i in range(15):
            sum = sum + binaryParams[i]
        binSum = bin(sum)[2:] # [2:] excludes the 0b in 0b01010111
        x = len(binSum)-8
        
        return int(binSum[x:], 2)


# def main():
#     serial = serialComm()
#     dd = User("dd")
    
#     if serial.attempt_connect():
#         print("connected")
#         #serial.send_packet(dd)
#         time.sleep(2)
#         serial.ser.close()

    

# main()


