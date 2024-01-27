import serial
import time

# تنظیمات پورت سریال
arduino_port = 'COM5'  # تغییر به پورت متناسب با سیستم شما
baud_rate = 9600

# اتصال به Arduino
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

def turn_on_led():
    # ارسال دستور روشن کردن به آردوینو
    ser.write(b'ON')
    print("LED روشن شد.")

def turn_off_led():
    # ارسال دستور خاموش کردن به آردوینو
    ser.write(b'OFF')
    print("LED خاموش شد.")

try:
    while True:
        command = input("Enter 'on' to turn on the LED, 'off' to turn it off, or 'exit' to quit: ")
        
        if command.lower() == 'on':
            turn_on_led()
        elif command.lower() == 'off':
            turn_off_led()
        elif command.lower() == 'exit':
            break
        else:
            print("دستور ناشناخته. لطفاً مجدداً تلاش کنید.")
except KeyboardInterrupt:
    pass
finally:
    # بستن اتصال به پورت سریال
    ser.close()
    print("اتصال به آردوینو بسته شد.")
