from socket import *
import random
import json
import time
import datetime
# Done
# Has a problem if we close the clientSocket.
# Could make a try exept if its a problem

REST_URL = "" # "https://udpexercise2rest20221101164840.azurewebsites.net"

class AirSensor:
    def __init__(self):
        self.room = 12
        self.timestamp = json.dumps(datetime.datetime.now(), default=str)
        self.co2_meassurement = random.randint(989, 1100) #Call measurement here


# Information about serverç
serverPort = 10100
clientSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

while True:  # Broadcast speed_data
    air_data = AirSensor()
    air_data_json = json.dumps(air_data.__dict__)
    clientSocket.sendto(air_data_json.encode(), (serverName, serverPort))
    time.sleep(round(random.uniform(0.5, 3)))
    # clientSocket.close()
    