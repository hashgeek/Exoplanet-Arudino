/*
 * kepler visulizer
 */
#include <Servo.h> 
#define PLANET 11

int ledPin = 6;   // LED connected to digital pin 6.
int buzzerPin = 8;// Piezo buzzer connected to digital pin 8.
Servo orbit;

void setup(){
  // initialize the serial communications:
  Serial.begin(9600);
  orbit.attach(PLANET); // Full rotation servo is connected to pin 11.
  pinMode(ledPin, OUTPUT);
  
}

void loop()
{
  byte fadeValue;
  
  // when characters arrive over the serial port...
  if (Serial.available()) {
      orbit.write(95);
      fadeValue = Serial.read();
      analogWrite(ledPin, fadeValue);
      tone(buzzerPin,fadeValue);
      }
}
