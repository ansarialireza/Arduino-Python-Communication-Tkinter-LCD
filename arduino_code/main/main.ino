#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
    lcd.begin(16, 2);
    Serial.begin(9600); // شروع ارتباط با سریال با سرعت 9600 بیت در ثانیه
}

void loop() {
    if (Serial.available() > 0) {
        // دریافت کلمه از سریال
        String receivedWord = Serial.readString();

        // نمایش کلمه بر روی LCD
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(receivedWord);
        Serial.println(receivedWord);


        // حرکت افقی
        for (int i = 0; i < 16; i++) {
            lcd.scrollDisplayLeft();
            delay(400);
        }

        // ارسال تأیید به کامپیوتر
        Serial.println("Word received successfully");
    }
}
