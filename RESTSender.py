import configparser
from  socket import *
import requests
import json
import AirSensor_class


# serverPort = 10100
# serverSocket = socket(AF_INET, SOCK_DGRAM)
# serverSocket.bind(("", serverPort))
# print("The server is ready to receive")

# https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/

def post_to_rest(message): #! Here we get int, so must use class
    co2_object = AirSensor_class.Sensor_co2(message)
    co2_object_json = json.dumps(co2_object.__dict__)
    response = requests.post(
        f"{get_rest_url_from_config()}/api/air", json=json.loads(co2_object_json) # Maybe dont need json.loads
    )
    #print(response.json())
    return

def get_rest_url_from_config():
    config_obj = configparser.ConfigParser()
    config_obj.read('configfile.ini')
    rest_connection = config_obj['rest_connection']
    return rest_connection['rest_url']

post_to_rest(1)

