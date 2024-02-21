#include <Stepper.h>
#include <ESP8266WiFi.h>

Stepper stepperMotor(STEPS_PER_REV, PIN1, PIN2, PIN3, PIN4);

void setup() {
  Serial.begin(9600);
  WiFi.begin(ssid, password);
  stepperMotor.setSpeed(60);
}

void loop() {
  if (newDataAvailable()) {
    processData(receivedData);
  }
  if (conditionMetForMovement()) {
    stepperMotor.step(stepsToMove);
  }
  if (pointerInAlertArea()) {
    triggerVibration();
  }
}

void processData(String data) { }
bool newDataAvailable() { return true; }
bool conditionMetForMovement() { return true; }
int stepsToMove = calculateSteps(receivedData);
bool pointerInAlertArea() { return true; }
void triggerVibration() { }
int calculateSteps(String data) { return 100; }
