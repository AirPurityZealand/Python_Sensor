from socket import *
import requests
from _thread import *

serverPort = 10100
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("The server is ready to receive")



def server_listen(): # Run me as thread
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        speedtrap_message = message.decode()
        print(speedtrap_message)

server_listen()