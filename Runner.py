import AirSensor
import RESTSender
import time

# set timer
def set_start_time():
    global start_time
    start_time = time.perf_counter()

# get elapsed time in min
def get_elapsed_time_min():
    return ((time.perf_counter() - start_time) / 3600)


def run():

    # get measurement from sensor
    co2_value = AirSensor.measure_co2()

    # set bool weaher measurement is bad
    co2_value_good = True

    if co2_value > 1000:
        co2_value_good = False
    else:
        co2_value_good = True

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


while True:
    run()
    time.sleep(5)
