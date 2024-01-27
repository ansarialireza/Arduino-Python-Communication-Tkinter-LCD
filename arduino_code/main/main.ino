#include <LiquidCrystal.h> 
int rs = 2, en = 3, d4 = 4, d5 = 5, d6 = 6, d7 = 7; 
LiquidCrystal lcd(rs, en, d4, d5, d6, d7); 

void setup() {
lcd.begin(16, 2);
}

void loop() {
lcd.setCursor(0,0);
lcd.print(".........ir");
lcd.setCursor(5,1);
lcd.print("IRAN");
delay(1000);
lcd.clear(); 
}