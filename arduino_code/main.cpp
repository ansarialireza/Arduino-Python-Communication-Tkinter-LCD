#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.print("Arduino LCD");
}

void loop() {
  if (Serial.available() > 0) {
    String receivedData = Serial.readStringUntil('\n');
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Received: ");
    lcd.setCursor(0, 1);
    lcd.print(receivedData);
  }
}
