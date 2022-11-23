from socket import *
import random
import json
import time
import datetime
# Done
# Has a problem if we close the clientSocket.
# Could make a try exept if its a problem


class AirSensor:
    def __init__(self):
        self.room = 12
        self.timestamp = json.dumps(datetime.datetime.now(), default=str)
        self.co2 = random.randint(1, 101)


# Information about serverç
serverName = "255.255.255.255"  # For broadcasting
serverPort = 10100
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)  # Broadcaster

while True:  # Broadcast speed_data
    air_data = AirSensor()
    air_data_json = json.dumps(air_data.__dict__)
    clientSocket.sendto(air_data_json.encode(), (serverName, serverPort))
    time.sleep(round(random.uniform(0.5, 3)))
    # clientSocket.close()
    