import time
import random


class Device:

    def __init__(self,name):
        self.name = name


class StateMachine:
    def __init__(self):
        print("Pump: Init")
        self.state = "Idle"
        self.is_running = False


    def set_state(self, new_state):
        print(f"Pump: from {self.state} to {new_state}")
        if new_state == "Running":
            self.is_running = True
        elif new_state == 'Idle':
            self.is_running = False
        self.state = new_state

    def start_pump(self):
        self.set_state("Running")
        print(f"Pump: Started")

    def stop_pump(self):
        self.set_state("Idle")
        print(f"Pump: Stopped")

    def take_sensor_reading(self):
        fake_sense = random.randrange(0,100)
        return fake_sense

    def run(self):
        if self.state == "Running":
            if not self.is_running:
                self.start_pump()

            reading = self.take_sensor_reading()
            if reading >= 75:
                print(f"Pump: Enough Water: {reading}")
                self.stop_pump()

        elif self.state == "Idle":
            reading = self.take_sensor_reading()

            if reading <= 10:
                print(f"Pump: Not Enough Water: {reading}")
                self.start_pump()


# Interaction mechanism
def control_device(device_machine):
    if device_machine.state == "Idle":
        user_input = input("Enter '1' to start the device, '2' to stop: ")
        if user_input == '1':
            device_machine.set_state("Running")
        elif user_input == '2':
            device_machine.set_state("Idle")
    elif device_machine.state == 'Running':
        pass


if __name__ == "__main__":
    device = StateMachine()
    device.set_state("Running")

    while True:
        device.run()

        # Handle user interaction
        # control_device(device)

        if device.state == "Shutdown":
            break

        time.sleep(0.5)