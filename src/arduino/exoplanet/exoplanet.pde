/*
 * kepler visulizer
 */
int ledPin = 9;   // LED connected to digital pin 9
int buzzerPin = 8;// Piezo buzzer connected to digital pin 8.

void setup(){
  // initialize the serial communications:
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  byte fadeValue;
  // when characters arrive over the serial port...
  if (Serial.available()) {
    // wait a bit for the entire message to arrive
      fadeValue = Serial.read();
      analogWrite(ledPin, fadeValue);
      tone(buzzerPin,fadeValue);
      }
}
