from  socket import *
import requests
import json
import AirSensor_class
import ConfigReader

def post_to_rest(message):
    co2_object = AirSensor_class.Sensor_co2(message)
    co2_object_json = json.dumps(co2_object.__dict__)
    response = requests.post(
        f"{ConfigReader.get_from_config('rest_connection', 'rest_url')}/api/Air", json=json.loads(co2_object_json)
    )
    print(f"{response.status_code} {response}")

