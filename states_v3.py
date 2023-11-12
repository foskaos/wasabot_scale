import time
import random


class PumpStateMachine:
    def __init__(self):
        print("Pump: Init\n")
        self.state = "Idle"
        self.is_running = False

    def set_state(self, new_state):
        print(f"Pump: from {self.state} to {new_state}")
        if new_state == "Running":
            self.is_running = True
        elif new_state == "Idle":
            self.is_running = False
        self.state = new_state

    def start_pump(self):
        print("Pump: Starting")
        self.set_state("Running")

    def stop_pump(self):
        self.set_state("Idle")
        print("Pump: Stopped")

    def tick(self):
        if self.state == "Running":
            print('Pump: Running')
            if not self.is_running:
                self.start_pump()


        elif self.state == "Idle":
            print('Pump: Idle')
            if self.is_running:
                self.stop_pump()



class ReservoirStateMachine:
    def __init__(self):
        print("Reservoir: Init")
        self.state = "Init"
        self.weight = self.read_weight()
        print(f'Reservoir: Starting with {self.weight} in res')

    def set_state(self, new_state):
        print(f"Reservoir: from {self.state} to {new_state}")
        if new_state == "Full":
            pass
        elif new_state == "Empty":
            pass
        self.state = new_state

    def read_weight(self):
        if self.state == "Init":
            fake_sense = random.randrange(50, 75)
            self.set_state('Full')
        else:
            fake_sense = self.weight  # random.randrange(0, self.weight+1)
        return fake_sense

    def tick(self):
        reading = self.read_weight()
        self.weight = reading

        if self.state == 'Full':
            if self.weight <= 10:
                print('new weight under 10')
                self.set_state('Empty')
        elif self.state == "Empty":
            pass  # The reservoir is full


class Irrigator:

    def __init__(self, pump, res):
        self.pump = pump
        self.res = res
        self.target_weight = 0
        self.cumulative_weight_dispensed = 0
        self.state = "Idle"
        self.is_running = False

    def set_state(self, new_state):
        print(f"Irrigator: from {self.state} to {new_state}")
        if new_state == "Watering":
            self.is_running = True
        elif new_state == "Idle":
            self.is_running = False
        self.state = new_state

    def start_watering(self):
        print("Irrigator: Starting")
        self.set_state("Watering")
        self.pump.start_pump()

    def stop_watering(self):
        self.set_state("Idle")
        print("Irrigator: Stopped")

    def set_target_weight(self, target_weight):
        if target_weight > 0:
            self.target_weight = self.res.weight - target_weight
            print(f"Irrigator: Target weight set to {self.target_weight} grams")
        else:
            print(f"Irrigator can stop")
            self.target_weight = 0

    def tick(self):

        if self.state == "Watering":
            print(f'Irrigator: Watering Plants to target of {self.target_weight}')

            if not self.is_running:
                self.start_watering()

            if self.pump.state == 'Running':  # simulate water coming out
                self.res.weight -= 1

            if self.res.state == 'Empty':
                self.pump.stop_pump()
                print('Refill Reservoir')

            if self.target_weight >= self.res.weight:
                print(f"Irrigator: Reached target Weight of {self.target_weight} with {self.res.weight}")
                self.pump.stop_pump()
                self.set_target_weight(0)
                self.stop_watering()

            self.res.tick()
            self.pump.tick()


        elif self.state == "Idle":
            print('Irrigator: Idle')
            if self.is_running:
                self.stop_watering()


# Create a single instance of the StateMachine
irig = Irrigator(PumpStateMachine(), ReservoirStateMachine())
print('starting control loop\n')
while True:
    # Check the weight of the reservoir
    weight = irig.res.weight
    print(f"Current weight: {irig.res.weight} grams, target = {irig.target_weight}")

    if weight > 50:
        if irig.state != 'Watering':
            irig.set_target_weight(8)
            irig.start_watering()
    # Update the state machine
    irig.tick()
    time.sleep(1)  # Adjust the loop interval as needed
    print()