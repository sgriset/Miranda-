// Tiny 85 Co-Processor that works with EZ1 MaxSonar
// and the Raspberry Pi Zero
// Part of the Miranda Project
// Version 1.0
// Steve Griset April 29, 2018




// HARDWARE: EZ1 Hook up 
// Make the following connections between the EZ1 and the Arduino
// +5V - +5V
// GND - GND
// AN - Analog In 0

// HARDWARE:  Tiny85 Hook up
// PIN 0 (PWM) Analog Output to an LED
// PIN 3 (A3)  Analog Input 
// PIN 1 (PWM) Analog Out put to Raspberry Pi Circuit

  
// OPERATIONS: Circuit analog in (A3) looks for any object that is within 8 inches of EZ1 Sensor
// The LED on pin 0 goes off, LED and circuit on pin 1 goes high singling to Raspberry Pi a object is near take evasive maneuvers  

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  int pwmPin = 0;
  int pwmPin2 = 1; 
  int analogInPin = A3;
  int sensor, inches, x;

  pinMode(pwmPin, OUTPUT);
  pinMode(pwmPin2, OUTPUT);
  pinMode(analogInPin, INPUT);

  analogWrite(pwmPin, 255);
  analogWrite(pwmPin2, 0);
  
  

  sensor = analogRead(analogInPin); // Read analog voltage on pin 3 (A3)
  inches = sensor / 2;

  if (inches < 8)
  {
    analogWrite(pwmPin, 0);
    analogWrite(pwmPin2, 255);
    delay(1000);
  }

}
