from datetime import *
import json
import configparser
import ConfigReader

class Sensor_co2:
    def __init__(self, co2_measurement):
        self.roomId = ConfigReader.get_from_config('sensor_local', 'room_id')
        self.timeStamp = json_serial(datetime.now())
        self.co2 = co2_measurement


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))