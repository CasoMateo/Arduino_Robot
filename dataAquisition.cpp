#include <Servo.h>

int in1 = 10;
int in2 = 9;
int in3 = 6;
int in4 = 5;
const int EchoPin = 11; 
const int TriggerPin = 4;
long duration;
int distance;

Servo servomotor;

void setup() {

  Serial.begin(9600);

  pinMode(in1, OUTPUT); 
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(TriggerPin, OUTPUT);
  pinMode(EchoPin, INPUT);
  servomotor.attach(3);
  

}
int ping(int TriggerPin, int EchoPin, int position_) {

  servomotor.write(position_);
  
  digitalWrite(TriggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(TriggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(TriggerPin, LOW);

  duration = pulseIn(EchoPin, HIGH);

  distance = duration * 0.034 / 2; 

  return distance;
}

int stop_() {

  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW); 
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW); 
 
}
  
void loop() {
  int cm;
  cm = ping(TriggerPin, EchoPin, 90);

  if (cm >= 50) {
    digitalWrite(in1, HIGH); 
    digitalWrite(in2, LOW);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);

  }

  else {
    stop_();

    Serial.write('x' + ping(TriggerPin, EchoPin, 0));
    Serial.write('y' + ping(TriggerPin, EchoPin, 180));

  
    if(Serial.available() > 0) {
      int message;
      message = Serial.read();

      if (message == 'a') { 
     
        digitalWrite(in3, HIGH);
        digitalWrite(in4, LOW);
         
      }

      if (message == 'b') { 
        
        digitalWrite(in1, HIGH); 
        digitalWrite(in2, LOW);

      }
    }
  }
}
 


 

    
