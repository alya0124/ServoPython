#include <Servo.h>

Servo mi_servo;  // create Servo object to control a servo

void setup() {
  Serial.begin(9600);
  mi_servo.attach(8); 
}

void loop() {

  if (Serial.available() > 0){
    int angulo = Serial.parseInt();
    mi_servo.write(angulo);  
    Serial.println("Ángulo: " + String(angulo));
    delay(15);  
  }
      
}