from gpiozero import Button
import subprocess

# Initialize the button (GPIO2, Pin 3)
button = Button(2)

# Path to the Python interpreter within the virtual environment
venv_python = "/home/deep/Fire_detection/venv/bin/python3"

# Wait for the button press
print("Waiting for button press...")
button.wait_for_press()

# Execute fire.py using the Python interpreter from the virtual environment
print("Button pressed. Running fire.py...")
subprocess.run([venv_python, "fire.py"])

print("Script execution completed.")
