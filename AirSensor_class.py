from datetime import *
import json
import random


class Sensor_co2:
    def __init__(self, co2_measurement):
        self.room = "P0"
        self.timestamp = json.dumps(datetime.datetime.now(), default=str)
        self.co2_meassurement = co2_measurement
