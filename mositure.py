# import required modules
from machine import ADC, Pin

import time

# use variables instead of numbers:
soil = ADC(Pin(26))  # Soil moisture PIN reference

# Calibraton values
min_moisture = 18004
max_moisture = 49852

readDelay = 0.5  # delay between readings

adc_readings =[]
counter = 0
try:
    while True:

        # read moisture value and convert to percentage into the calibration range
        moisture = (max_moisture - soil.read_u16()) * 100 / (max_moisture - min_moisture)
        adc_readings.append(soil.read_u16())
        # print values
        print("moisture: " + "%.2f" % moisture + "% (adc: " + str(soil.read_u16()) + ")")
        counter += 1

        time.sleep(readDelay)  # set a delay between readings
        if counter >1000:
            print(max(adc_readings),min(adc_readings))
            break
except KeyboardInterrupt:
    # Code to run when a keyboard interrupt is caught
    print('Loop interrupted by the user')
    print(max(adc_readings), min(adc_readings))
