import configparser
from  socket import *
import requests
import json
import AirSensor_class
import ConfigReader


# serverPort = 10100
# serverSocket = socket(AF_INET, SOCK_DGRAM)
# serverSocket.bind(("", serverPort))
# print("The server is ready to receive")

# https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/

def post_to_rest(message):
    co2_object = AirSensor_class.Sensor_co2(message)
    co2_object_json = json.dumps(co2_object.__dict__)
    response = requests.post(
        f"{ConfigReader.get_from_config('rest_connection', 'rest_url')}/api/Air", json=json.loads(co2_object_json) # Maybe dont need json.loads
    )
    print(f"{response.status_code} {response}")

