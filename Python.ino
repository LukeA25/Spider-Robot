//#include <cvzone.h>
#include <Servo.h>

Servo myservo;
//SerialData serialData(1, 3);

//int valsRec[1];

void setup() {
  myservo.attach(9);
//  serialData.begin();
}

void loop() {
//  serialData.Get(valsRec);
//valsRec[0]
  myservo.write(90);
  delay(15);
}
