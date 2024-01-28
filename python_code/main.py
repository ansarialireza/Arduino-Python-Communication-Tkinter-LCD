import tkinter as tk
from tkinter import messagebox
import serial
import time

# اتصال به پورت سریال که Arduino به آن وصل شده است
ser = serial.Serial('COM5', 9600)  # COMx را با پورت واقعی متصل به Arduino جایگزین کنید

# انتظار برای اتصال Arduino
time.sleep(2)

def send_text_to_lcd():
    # دریافت متن از باکس و ارسال به Arduino برای نمایش در LCD
    text_line1 = entry_line1.get()
    text_line2 = entry_line2.get()

    # ارسال متن به Arduino برای نمایش در LCD
    ser.write(text_line1.encode('utf-8'))
    ser.write(b'\n')  # ارسال کاراکتر جداکننده بین خطوط
    ser.write(text_line2.encode('utf-8'))

    messagebox.showinfo("Success", "Text sent to Arduino successfully!")

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("Arduino LCD Display")

# ایجاد باکس‌ها و دکمه
label_line1 = tk.Label(root, text="Line 1:")
entry_line1 = tk.Entry(root)

label_line2 = tk.Label(root, text="Line 2:")
entry_line2 = tk.Entry(root)

send_button = tk.Button(root, text="Send to Arduino", command=send_text_to_lcd)

# تنظیم موقعیت باکس‌ها و دکمه در پنجره
label_line1.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_line1.grid(row=0, column=1, padx=10, pady=10)

label_line2.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_line2.grid(row=1, column=1, padx=10, pady=10)

send_button.grid(row=2, column=1, pady=20)

# حلقه اصلی پنجره
root.mainloop()

# بستن اتصال سریال هنگام بسته شدن پنجره
ser.close()
