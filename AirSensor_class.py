from datetime import *
import json
import configparser


class Sensor_co2:
    def __init__(self, co2_measurement):
        self.roomId = get_roomId_from_config()
        self.timeStamp = json_serial(datetime.now())
        self.co2 = co2_measurement


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

def get_roomId_from_config():
    config_obj = configparser.ConfigParser()
    config_obj.read('configfile.ini')
    sensor_local = config_obj['sensor_local']
    return sensor_local['room_id']

def test_class(co2_measurement = 1): #! For testing
    sensor_co2 = Sensor_co2(1)
    
    print(f"{sensor_co2.roomId}\n{sensor_co2.timeStamp}\n{sensor_co2.co2}")

def test_class_json(): #! Also testing
    sensor_co2 = Sensor_co2(1)
    co2_object_json = json.dumps(sensor_co2.__dict__)
    print(co2_object_json)