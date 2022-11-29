from socket import *
import random
import json
import time
import datetime
import AirSensor_class
# Done
# Has a problem if we close the clientSocket.
# Could make a try exept if its a problem

REST_URL = "" # "https://udpexercise2rest20221101164840.azurewebsites.net"


# Information about server
serverPort = 10100
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))


def send_current_measurement():
    air_data = AirSensor_class()
    air_data_json = json.dumps(air_data.__dict__)
    response = air_data_json.post(
        f"{REST_URL}/api/AirData", json=air_data_json)
    print(response.json())
    return

def send_measurement(air_data):
    air_data_json = json.dumps(air_data.__dict__)
    response = air_data_json.post(
        f"{REST_URL}/api/AirData", json=air_data_json)
    print(response.json())
    return
