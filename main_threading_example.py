import _thread
import machine
import time

import os


from time import sleep
uart = machine.UART(0, 9600)
print(uart)
b = None
msg = ""




internal_led = machine.Pin(25, machine.Pin.OUT)
analog_value = machine.ADC(28)
def function(i):
    while True:
        reading = analog_value.read_u16()
        print(f"{i}, I'm here in the second thread writing every second.")
        print(f"I'm reading: {reading}")
        time.sleep(0.5)
    # print(f"function called by thread {i}")
    # return

threads = []

# for i in range(1):
t = _thread.start_new_thread(function , ('hi!',))
    # threads.append(t)
    # t.start()
    # t.join()

while True:
    internal_led.toggle()
    time.sleep(0.25)
    if uart.any():
        b = uart.readline()
        print(type(b))
        print(b)
        try:
            msg = b.decode('utf-8')
            print(type(msg))
            print(">> " + msg)
        except:
            pass