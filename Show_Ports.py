import serial.tools.list_ports

# Display a list of available ports
ports = serial.tools.list_ports.comports()

# Iterate through the list of ports and print information for each port
for port, desc, hwid in sorted(ports):
    print(f"Port: {port}, Description: {desc}, Hardware ID: {hwid}")
