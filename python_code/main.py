import tkinter as tk
import serial
import time

arduino_port = "/dev/ttyACM0"  # Change this to your Arduino port
arduino_baudrate = 9600

def send_data():
    entered_data = entry.get()
    print("Data entered:", entered_data)
    
    try:
        with serial.Serial(arduino_port, arduino_baudrate, timeout=1) as ser:
            ser.write(entered_data.encode() + b'\n')  # Add a newline character
            time.sleep(2)  # Wait for Arduino to process and respond
            response = ser.readline().decode().strip()
            print("Arduino response:", response)
    except serial.SerialException as e:
        print("Error communicating with Arduino:", e)

# Create the main window
window = tk.Tk()
window.title("Data Sender")

# Create an entry box for the data
entry = tk.Entry(window)
entry.pack(pady=10)

# Create a button to send the data
send_button = tk.Button(window, text="Send Data", command=send_data)
send_button.pack()

# Start the main loop
window.mainloop()
