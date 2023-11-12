from machine import Pin,UART
from hx711 import *
import time
# 1. initalise the hx711 with pin 10 as clock pin, pin
# 11 as data pin
hx = hx711(Pin(10), Pin(11))

# 2. power up
hx.set_power(hx711.power.pwr_up)

# 3. [OPTIONAL] set gain and save it to the hx711
# chip by powering down then back up
hx.set_gain(hx711.gain.gain_64)
hx.set_power(hx711.power.pwr_down)
hx711.wait_power_down()
hx.set_power(hx711.power.pwr_up)

# 4. wait for readings to settle
hx711.wait_settle(hx711.rate.rate_10)

# 5. read values

# # wait (block) until a value is read
# val = hx.get_value()
#
# # or use a timeout
# if val := hx.get_value_timeout(250000):
#     # value was obtained within the timeout period
#     # in this case, within 250 milliseconds
#     print(val)
uart = UART(0, 9600,timeout=500)

zero_avg = []
print('doing zero point')
# hx711.wait_settle(hx711.rate.rate_10)
# hx.get_value()
# hx.get_value()
for _ in range(100):
    hx711.wait_settle(hx711.rate.rate_10)

    val1 = hx.get_value()
    print(val1)
    zero_avg.append(val1)
    #time.sleep(0.15)

print('add weight')



time.sleep(4)
input("ready?")

w_avg = []
# hx711.wait_settle(hx711.rate.rate_10)
#
# hx.get_value()
# hx.get_value()
for _ in range(100):
    hx711.wait_settle(hx711.rate.rate_10)

    val2 = hx.get_value()
    print(val2)
    w_avg.append(val2)
    #time.sleep(0.15)




# or see if there's a value, but don't block if not
zero = sum(zero_avg[10:])/len(zero_avg[10:])
print('zero:',zero)
nine85 = sum(w_avg[10:])/len(w_avg[10:])
print('weighed:',nine85)
m = 1102.0 / (nine85 - zero)
print("m:",m)
b = -m * zero
print("b:",b)

input("take weight off")

reads = []
while True:

    val = hx.get_value()

    gr = (val*m) + b
    print(val,gr)

    reads.append(gr)
    if len(reads) == 20:
        print(val, gr)
        print()
        print('avg:', round(sum(reads)/20,1))
        reads = []




    # if val := hx.get_value_noblock():
    #     print(val)
        # if val >= int(0x800000):
        #     print('error')
        # else:
        #     if len(reads) <= 4:
        #         reads.append(val)
        #     else:
        #         print(sum(reads)/len(reads))
        #         reads = []
    #
    # if uart.any():
    #     print('uart available')
    #     b = uart.readline()
    #     msg = b.decode('utf-8')
    #     print(msg)
    #     if msg.strip() == 'bb':
    #         print('add command')
    #         cal = val




    time.sleep(0.15)
# 6. stop communication with HX711
hx.close()
