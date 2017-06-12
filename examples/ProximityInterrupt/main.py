#****************************************************************
# ProximityInterrupt.ino
# APDS-9960 RGB and Gesture Sensor
# Shawn Hymel @ SparkFun Electronics
# October 24, 2014
# https://github.com/sparkfun/APDS-9960_RGB_and_Gesture_Sensor
# Tests the proximity interrupt abilities of the APDS-9960.
# Configures the APDS-9960 over I2C and waits for an external
# interrupt based on high or low proximity conditions. Move your
# hand near the sensor and watch the LED on pin 13.
# Hardware Connections:
# IMPORTANT: The APDS-9960 can only accept 3.3V!
 
#  Arduino Pin  APDS-9960 Board  Function
 
#  3.3V         VCC              Power
#  GND          GND              Ground
#  A4           SDA              I2C Data
#  A5           SCL              I2C Clock
#  2            INT              Interrupt
#  13           -                LED
# Resources:
# Include Wire.h and SparkFun_APDS-9960.h
# Development environment specifics:
# Written in Arduino 1.0.5
# Tested with SparkFun Arduino Pro Mini 3.3V
# This code is beerware; if you see me (or any other SparkFun 
# employee) at the local, and you've found our code helpful, please
# buy us a round!
# Distributed as-is; no warranty is given.
# ****************************************************************/


import streams
streams.serial()
sleep(3000)

import APDS9960

APDS9960_INT    = D26  #Needs to be an interrupt pin
LED_PIN         = LED1 # LED for showing interrupt

#Constants
PROX_INT_HIGH   =  50  #Proximity level for interrupt
PROX_INT_LOW    = 0 #No far interrupt

#Global variables

proximity_data = 0;
isr_flag = 0;

 def interruptRoutine():
        global isr_flag
        if isr_flag==0:
            isr_flag = 1

onPinFall(APDS9960_INT,interruptRoutine)
pinMode(LED_PIN,OUTPUT)

print("---------------------------------------")
print("SparkFun APDS-9960 - ProximityInterrupt")
print("---------------------------------------")
  
# Initialize APDS-9960 (configure I2C and initial values)
sensor = APDS9960.APDS9960(I2C0)
sensor.initialize()
print("APDS-9960 initialization complete")

sensor.setProximityGain(PGAIN_2X))
print("Something went wrong trying to set PGAIN")
  

#Set proximity interrupt thresholds
sensor.apds.setProximityIntLowThreshold(PROX_INT_LOW)
print("Error writing low threshold")

sensor.setProximityIntHighThreshold(PROX_INT_HIGH) ) {
print("Error writing high threshold")

#Start running the APDS-9960 proximity sensor (interrupts)
sensor.enableProximitySensor(True)
print("Proximity sensor is now running")

while True:
    try:
        if isr_flag==1: #If interrupt occurs, print out the proximity level
            proximity_data = sensor.readProximity()
            print("Proximity detected! Level: ", proximity_data)
            
            #Turn on LED for a half a second
            digitalWrite(LED_PIN, HIGH)
            sleep(500)
            digitalWrite(LED_PIN, LOW)


            #Reset flag and clear APDS-9960 interrupt (IMPORTANT!)
            isr_flag = 0;
            sensor.clearProximityInt() 
    

