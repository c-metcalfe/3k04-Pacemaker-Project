import serial
import time
import User

class serialComm():
    def __init__(self):
        print("hrff")
        self.ser = serial.Serial()
        self.ser.port = "COM6"
        self.ser.baudrate = 115200
        self.ser.timeout = 2
        print("h")
        ### this is the port that it connects to on my laptop -colin

    def attempt_connect(self):
        self.ser.open()
        if not self.ser.is_open: 
            print("Failed to open port")
            return False
        return True
        
    def start_reading(self):
        while True:
            data = self.ser.read(16)
            print(":", data)
            time.sleep(1)

    
        
    
    def send_packet(self, user): # TODO send packet to pacemaker in correct format 
        
        binaryParams = bytearray()
        binaryParams.append(bin(int(user.mode))[2:])

        


        

        
    # checksum should be bitwise addition of bits 1-15
        

def checksum(binaryParams):
        sum = 0
        for i in range(15):
            sum = sum + binaryParams[i]
        binSum = bin(sum)[2:] # [2:] excludes the 0b in 0b01010111
        x = len(binSum)-8
        
        return int(binSum[x:], 2)


def main():
    # ser = serialComm()
    # if ser.attempt_connect():
    #     ser.start_reading()
    user = User.UserClass("dd")

    paramsList = [user.mode,user.lowerRateLimit,user.upperRateLimit,int(10*user.atrialAmplitude),
                int(10*user.ventAmplitude), user.atrialPulseWidth, user.ventPulseWidth, int(user.VRP /10),
                int(user.ARP /10), user.activityThreshold, user.reactionTime, user.responseFactor, user.recoveryTime,
                0,0]# 0's are reserved
    binaryParams = bytearray(paramsList)
    
    binaryParams.append(checksum(binaryParams))
    
    
    # binaryParams.append(user.mode)
    # binaryParams.append(user.lowerRateLimit)
    # binaryParams.append(user.upperRateLimit)
    # binaryParams.append(int(10*user.atrialAmplitude))
    # binaryParams.append(int(10*user.ventAmplitude))
    # binaryParams.append(user.atrialPulseWidth)
    # binaryParams.append(user.ventPulseWidth)
    # binaryParams.append(int(user.VRP /10))
    # binaryParams.append(int(user.ARP /10))
    # binaryParams.append(user.activityThreshold)
    # binaryParams.append(user.reactionTime)
    # binaryParams.append(user.responseFactor)
    # binaryParams.append(user.recoveryTime)
    # print(paramsList)
    print(binaryParams)
    for byte in binaryParams:
        print(byte)

main()


