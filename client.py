from socket import *
from datetime import datetime
import time


serverName = '127.0.0.1'
serverPort = 1453
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.connect((serverName,serverPort))
message = "ping"
rtt=0
for i in range(1,11,1):
    clientSocket.sendto(message.encode(),(serverName, serverPort))    
    clientSocket.settimeout(1)
    a = datetime.now()
    time.sleep(1)
    try:
        modifiedMessage, serverAddress =clientSocket.recvfrom(2048)
        print(str(i)+". Mesaj "+str(modifiedMessage))  
    except Exception:
        print("Timeout oldu") 
  
    b=datetime.now()
    rtt=b-a
    print("\t RTT : "+str(rtt))       
  
   

clientSocket.close()