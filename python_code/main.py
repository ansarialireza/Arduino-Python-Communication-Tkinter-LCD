import tkinter as tk
from tkinter import messagebox
import serial
import time
import threading
import tkinter.scrolledtext as scrolledtext

class ArduinoLCDApp:
    def __init__(self,port,baud_rate, master):
        self.master = master
        self.port=port
        self.baud_rate=baud_rate
        # master.title("Arduino LCD Display")

        # Serial connection to Arduino
        self.ser = serial.Serial(port,baud_rate)  # Replace 'COMx' with the actual port connected to Arduino
        time.sleep(2)

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry widgets
        self.label_line1 = tk.Label(self.master, text="Line 1:")
        self.entry_line1 = tk.Entry(self.master)

        self.label_line2 = tk.Label(self.master, text="Line 2:")
        self.entry_line2 = tk.Entry(self.master)

        # Button to send text to Arduino
        self.send_button = tk.Button(self.master, text="Send to Arduino", command=self.send_text_to_lcd)

        # Set positions of widgets in the window
        self.label_line1.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_line1.grid(row=0, column=1, padx=10, pady=10)

        self.label_line2.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_line2.grid(row=1, column=1, padx=10, pady=10)

        self.send_button.grid(row=2, column=1, pady=20)

        # Label to display received messages from Arduino
        self.received_message_label = tk.Label(self.master, text="")
        self.received_message_label.grid(row=3, column=0, columnspan=2, pady=10)

        # ScrolledText to display received messages with scrolling
        self.scrolled_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=40, height=10)
        self.scrolled_text.grid(row=4, column=0, columnspan=2, pady=10)

        # Parallel thread to receive commands from Arduino
        self.receive_thread = threading.Thread(target=self.receive_from_arduino, daemon=True)
        self.receive_thread.start()

    def send_text_to_lcd(self):
        # Get text from Entry widgets and send to Arduino
        text_line1 = self.entry_line1.get()
        text_line2 = self.entry_line2.get()

        self.ser.write(text_line1.encode('utf-8'))
        self.ser.write(b'\n')  # Send newline character as a separator between lines
        self.ser.write(text_line2.encode('utf-8'))

        messagebox.showinfo("Success", "Text sent to Arduino successfully!")

    def receive_from_arduino(self):
        while True:
            try:
                message = self.ser.readline().decode('utf-8').rstrip('\r\n')
                if message:
                    self.received_message_label.config(text=f"Received message from Arduino: {message}")
                    self.scrolled_text.insert(tk.END, f"{message}\n")
                    self.scrolled_text.see(tk.END)  # Scroll to the last line

            except serial.SerialException:
                break

    def close_serial_connection(self):
        # Close serial connection when the window is closed
        self.ser.close()

if __name__ == "__main__":
    root = tk.Tk()
    port = 'COM10'  # COM10 should be a string
    baud_rate = 9600
    app = ArduinoLCDApp(port, baud_rate, root)
    root.protocol("WM_DELETE_WINDOW", app.close_serial_connection)
    root.mainloop()
