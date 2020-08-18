import socket
import random
import time
srvPort = 1453
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', srvPort))
print("server up")
while 1:  
    randNumber = random.randint(1,100)
    if randNumber<10 or randNumber>70: #Paket kaybolması (simülasyon)
        clientMessage,clientAddress = serverSocket.recvfrom(2048)
        responseMessage ="pong"
        serverSocket.sendto(responseMessage.encode(), clientAddress)             
    else:        
        time.sleep(1)
        continue

   
    