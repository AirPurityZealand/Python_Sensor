from datetime import *
import json
import random


class Sensor_co2:
    def __init__(self, co2_measurement):
        self.roomId = "P0"
        self.timeStamp = json_serial(datetime.now())
        self.co2 = co2_measurement


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


def test_class(co2_measurement = 1): # For testing
    sensor_co2 = Sensor_co2(1)
    
    print(f"{sensor_co2.RoomId}\n{sensor_co2.TimeStamp}\n{sensor_co2.Co2}")

def test_class_json(): # Also testing
    sensor_co2 = Sensor_co2(1)
    co2_object_json = json.dumps(sensor_co2.__dict__)
    print(co2_object_json)

#test_class()
test_class_json()