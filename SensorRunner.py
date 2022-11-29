import random
import time
import AirPuritySimulatorUDP


# Must measure every 5 sec
#   if data bad light LED
# Must send data every 15 min
# If data bad, send again in 5 min
def set_start_time():
    global start_time
    start_time = time.perf_counter()

def measure_air():
    co2_meassurement = random.randint(989, 1100) #Call measurement here
    return co2_meassurement

def set_update_timer():
    co2_meassurement = measure_air()
    co2_low_value, co2_high_value = 800, 1000
    if co2_meassurement <= co2_low_value or co2_meassurement >= co2_high_value:
        update_timer = 5*60
    else: 
        update_timer = 15*60
        return update_timer
    
last_measurement_was_bad = False
def runner():
    
    # HERE method that lights led if measurement is bad
    
    elapsed_time = ((time.perf_counter() - start_time)/60)
    
    if elapsed_time >  and last_measurement_was_bad:
        AirPuritySimulatorUDP.send_current_measurement()
        set_start_time()
    elif elapsed_time > 15.0:
        AirPuritySimulatorUDP.send_current_measurement()
        set_start_time()

    time.sleep(5)
    runner()
    
    