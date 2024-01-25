import tkinter as tk
from serial import Serial
import time

# تنظیمات اتصال سریال
arduino_port = "COM5"  # تنظیمات پورت اردوینو (ممکن است تغییر کند)
baud_rate = 9600

# تابع ارسال دستور به Arduino
def send_to_arduino(word):
    with Serial(arduino_port, baud_rate, timeout=1) as ser:
        ser.write(word.encode('utf-8'))
        time.sleep(1)  # انتظار کوتاه برای اطمینان از انجام کامل ارسال

# تابع برای کنترل دکمه ارسال
def send_button_click():
    user_input = entry.get()
    send_to_arduino(user_input)

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("ارسال کلمه به ال سی دی")

# ایجاد ویجت‌ها
label = tk.Label(root, text="کلمه را وارد کنید:")
entry = tk.Entry(root)
send_button = tk.Button(root, text="ارسال به ال سی دی", command=send_button_click)

# پرانت‌ها برای تعیین موقعیت ویجت‌ها در صفحه
label.pack()
entry.pack()
send_button.pack()

# شروع حلقه رویداد
root.mainloop()
