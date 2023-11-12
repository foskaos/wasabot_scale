import time

class StateMachine:
    def __init__(self):
        self.state = "Idle"
        self.running = False

    def set_state(self, new_state):
        self.state = new_state

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def run(self):
        if self.state == "Idle":
            pass  # Implement idle state logic here

        elif self.state == "Running":
            pass  # Implement running state logic here

        elif self.state == "Error":
            pass  # Implement error state logic here

        # Add more states and logic as needed

# Interaction mechanism
def control_device(device_machine, device_name):
    
    user_input = input(f"Enter '1' to start {device_name}, '2' to stop, 'q' to quit: ")

    if user_input == '1':
        device_machine.set_state("Running")
        device_machine.start()
    elif user_input == '2':
        device_machine.set_state("Idle")
        device_machine.stop()
    elif user_input == 'q':
        device_machine.set_state("Shutdown")
    else:
        pass

if __name__ == "__main__":
    water_dispenser = StateMachine()
    fan = StateMachine()

    water_dispenser.set_state("Idle")
    fan.set_state("Idle")

    while True:
        water_dispenser.run()
        fan.run()

        # Handle user interaction
        control_device(water_dispenser, "Water Dispenser")
        control_device(fan, "Fan")

        if water_dispenser.state == "Shutdown" and fan.state == "Shutdown":
            break
