import serial
import time
import User

class serialComm():
    def __init__(self):
        self.ser = serial.Serial()
        self.ser.port = "COM6"
        self.ser.baudrate = 115200
        self.ser.timeout = 2
        ### this is the port that it connects to on my laptop -colin

    def attempt_connect(self):
        self.ser.open()
        if not self.ser.is_open: 
            print("Failed to open port")
            return False
        return True
        
    def start_reading(self):
        for i in range(10):
            data = self.ser.read(16)
            print(":", data)
            time.sleep(1)
        self.ser.close()
    
        
    
    def send_packet(self, user): # send packet to pacemaker in correct format 

        paramsList = [user.mode,user.lowerRateLimit,user.upperRateLimit,int(10*user.atrialAmplitude),
                int(10*user.ventAmplitude), user.atrialPulseWidth, user.ventPulseWidth, int(user.VRP /10),
                int(user.ARP /10), user.activityThreshold, user.reactionTime, user.responseFactor, user.recoveryTime,
                0,0]# 0's are reserved
        binaryParams = bytearray(paramsList)
    
        binaryParams.append(checksum(binaryParams))

        self.ser.write(binaryParams)

        

def checksum(binaryParams):
        sum = 0
        for i in range(15):
            sum = sum + binaryParams[i]
        binSum = bin(sum)[2:] # [2:] excludes the 0b in 0b01010111
        x = len(binSum)-8
        
        return int(binSum[x:], 2)


def main():
    serial = serialComm()
    dd = User("dd")
    if serial.attempt_connect():
        serial.send_packet(dd)
    

main()


