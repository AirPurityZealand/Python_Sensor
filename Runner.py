import Sensor
import RESTSender
import time
import Led_controller
start_time = 0.0
# set timer
def set_start_time():
    global start_time
    start_time = time.perf_counter()

# get elapsed time in min
def get_elapsed_time_min():
    global start_time
    return ((time.perf_counter() - start_time) / 60)

def run():

    # get measurement from sensor
    co2_value = Sensor.measure_co2()

    # set bool weaher measurement is bad
    co2_value_good = True

    #if co2_value > 1000:
    if co2_value == 1:
        co2_value_good = False
        Led_controller.led_controller('on') # Turn led on
    else:
        co2_value_good = True
        Led_controller.led_controller('off') # Turn led off

    # if bool == bad and timer > 5min
    #   send measurement
    #   set timer
    if co2_value_good == False and get_elapsed_time_min() > 5.0:
        RESTSender.post_to_rest(co2_value)
        set_start_time()

    # if measurement == good and timer > 15min
    #   send measurement
    #   set timer
    if co2_value_good == True and get_elapsed_time_min() > 15.0:
        RESTSender.post_to_rest(co2_value)
        set_start_time()

# set_start_time() # Comment out to run once on startup. 
while True:
    run()
    time.sleep(0.5)