from  socket import *
from textwrap import indent
from post_threading import post_thread
import requests
import json
import AirSensor_class

REST_URL = "" # "https://udpexercise2rest20221101164840.azurewebsites.net"

serverPort = 10100
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("The server is ready to receive")

# https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/

def post_to_rest(message): #! Here we get int, so must use class
    co2_object = AirSensor_class.Sensor_co2(message)
    co2_object_json = json.dumps(co2_object.__dict__)
    response = requests.post(
        f"{REST_URL}/api/AirData", json=json.loads(message) # Maybe dont need json.loads
    )
    print(response.json())
    return


