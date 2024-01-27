import serial.tools.list_ports

# نمایش لیست پورت‌های در دسترس
ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print(f"Port: {port}, Description: {desc}, Hardware ID: {hwid}")
