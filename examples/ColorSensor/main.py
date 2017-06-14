# /****************************************************************
# ColorSensor.ino
# APDS-9960 RGB and Gesture Sensor
# Shawn Hymel @ SparkFun Electronics
# October 15, 2014
# https://github.com/sparkfun/APDS-9960_RGB_and_Gesture_Sensor
# Tests the color and ambient light sensing abilities of the 
# APDS-9960. Configures APDS-9960 over I2C and polls the sensor for
# ambient light and color levels, which are displayed over the 
# serial console.
# Hardware Connections:
# IMPORTANT: The APDS-9960 can only accept 3.3V!
 
#  Arduino Pin  APDS-9960 Board  Function
 
#  3.3V         VCC              Power
#  GND          GND              Ground
#  A4           SDA              I2C Data
#  A5           SCL              I2C Clock
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


import APDS9960
import stream

streams.serial()


#uint16_t 
ambient_light = 0;
red_light = 0;
green_light = 0;
blue_light = 0;


print("--------------------------------");
print("SparkFun APDS-9960 - ColorSensor");
print("--------------------------------");

sensor = APDS9960.APDS9960(I2C0)
sensor.initialize()
sensor.enableGestureSensor(True)

print("APDS-9960 initialization complete");

#Start running the APDS-9960 light sensor (no interrupts)
try:
    
    sensor.enableLightSensor(False)
    print("Light sensor is now running");
    
    #Wait for initialization and calibration to finish
    sleep(500);

except:
   print("Something went wrong during light sensor init!");



while True:
  
    #Read the light levels (ambient, red, green, blue)
    ambient_light = sensor.readAmbientLight()
    red_light = sensor.readRedLight() 
    green_light = sensor.readGreenLight()
    blue_light = sensor.readBlueLight(blue_light) ) {
    
    print("Ambient: ", ambient_light)
    print("Red: ", red_light)
    print(" Green: ", green_light)
    print(" Blue: ", blue_light)
    
    #Wait 1 second before next reading
    sleep(1000);
