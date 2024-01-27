// This code is written for Arduino Uno

const int ledPin = LED_BUILTIN;  // Use the built-in LED on pin 13

void setup() {
  Serial.begin(9600);  // Start serial communication
  pinMode(ledPin, OUTPUT);  // Set the LED pin as output
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = 0;
    Serial.readBytesUntil('\n', &receivedChar, 1);  // Read until newline character

    if (strcmp(receivedChar, "ON") == 0) {
      digitalWrite(ledPin, HIGH);  // Turn on the LED
      Serial.println("LED is ON");
    } else if (strcmp(receivedChar, "OFF") == 0) {
      digitalWrite(ledPin, LOW);  // Turn off the LED
      Serial.println("LED is OFF");
    }
  }
}
