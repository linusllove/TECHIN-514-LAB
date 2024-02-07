#include <WiFi.h>

// Pins for the ultrasonic sensor
const int triggerPin = 5;
const int echoPin = 18;
long duration;
int distance;

void setup() {
  Serial.begin(115200);
  // Set pin modes for ultrasonic sensor
  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  unsigned long startMillis = millis();
  bool shouldSleep = true; // Assume the system should sleep unless a close object is detected
  
  while (millis() - startMillis < 30000) { // 30-second measurement period
    distance = measureDistance();
    
    if (distance <= 50) {
      shouldSleep = false;
      break; // Object detected within 50 cm, no need to continue checking
    }
    
    delay(1000); // Delay between measurements
  }
  
  if (shouldSleep) {
    enterDeepSleep();
  }
}

int measureDistance() {
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  return duration * 0.034 / 2;
}

void enterDeepSleep() {
  Serial.println("Entering deep sleep for 30 seconds");
  esp_sleep_enable_timer_wakeup(30 * 1000000); // Time in microseconds
  esp_deep_sleep_start();
}
