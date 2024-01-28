#include <LiquidCrystal.h>
#include <Keypad.h>


LiquidCrystal lcd(A0, A1, A2, A3, A4, A5);

const byte ROWS = 4;
const byte COLS = 3;
char keys[ROWS][COLS] = {
    {'1', '2', '3'},
    {'4', '5', '6'},
    {'7', '8', '9'},
    {'*', '0', '#'}
};

byte rowPins[ROWS] = {10, 9, 8, 7};
byte colPins[COLS] = {13, 12, 11};


Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Hi, GitHub addr:");
  lcd.setCursor(0, 1);
  lcd.print(" ansarialireza");
}

void loop() {
  if (Serial.available() > 0) {
    String line1 = Serial.readStringUntil('\n');
    String line2 = Serial.readStringUntil('\n');
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(line1);
    lcd.setCursor(0, 1);
    lcd.print(line2);
  }

  char key = keypad.getKey();
  if (key) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("you sent:");
    lcd.setCursor(0, 1);
    lcd.print(key);
    Serial.print("Keypad: ");
    Serial.println(key);
  }
}
