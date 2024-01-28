#include <LiquidCrystal.h>

// تعریف پین‌های اتصال LCD به آردوینو
const int rs = 2, en = 3, d4 = 4, d5 = 5, d6 = 6, d7 = 7;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  // شروع کار با نمایشگر LCD با اندازه 16x2
  lcd.begin(16, 2);
  Serial.begin(9600);  // شروع اتصال سریال
}

void loop() {
  if (Serial.available() > 0) {
    // دریافت دستورات از پورت سریال
    String line1 = Serial.readStringUntil('\n');
    String line2 = Serial.readStringUntil('\n');

    // نمایش متن در خطوط مختلف LCD
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(line1);
    lcd.setCursor(0, 1);
    lcd.print(line2);
  }
}
