const int motionSensorPin = 3; 
unsigned long lastMotionTime = 0; 
unsigned long motionTimeout = 5000; 
bool motionDetected = false;

void setup() {
  Serial.begin(9600);
  pinMode(motionSensorPin, INPUT);
}

void loop() {
  int motionState = digitalRead(motionSensorPin);
  if (motionState == HIGH) {
    // Motion detected
    if (!motionDetected) {
      Serial.println("motion detected");
      motionDetected = true;
    }
    lastMotionTime = millis(); 
  } else {
    // No motion detected
    if (motionDetected && millis() - lastMotionTime >= motionTimeout) {
      Serial.println("No motion detected");
      motionDetected = false; 
    }
  }
  delay(100); 
}
