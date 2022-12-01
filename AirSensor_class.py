from datetime import *
import json
import random


class Sensor_co2:
    def __init__(self, co2_measurement):
        self.room = "P0"
        self.timestamp = json.dumps(datetime.now(), default=str)
        self.co2_meassurement = co2_measurement




def test_class(co2_measurement = 1): # For testing
    sensor_co2 = Sensor_co2(1)
    
    print(f"{sensor_co2.room}\n{sensor_co2.timestamp}\n{sensor_co2.co2_meassurement}")