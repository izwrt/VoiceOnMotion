// Pin connected to the output of the motion sensor
const int motionSensorPin = 3; // Change this to the pin your motion sensor is connected to

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT); // Configure built-in LED pin as output
  pinMode(motionSensorPin, INPUT);
}

void loop() {
  int motionState = digitalRead(motionSensorPin);
  if (motionState == HIGH) {
    Serial.println("Motion Detected"); // Send motion detection message to PC
    digitalWrite(LED_BUILTIN, HIGH); // Turn on built-in LED
    delay(1000); // Wait for 1 second
    digitalWrite(LED_BUILTIN, LOW); // Turn off built-in LED
    delay(1000); // Wait for 1 second
  }
}
