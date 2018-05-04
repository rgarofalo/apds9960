# /****************************************************************
# This example was written from this example of the sparkfun
# https://github.com/sparkfun/APDS-9960_RGB_and_Gesture_Sensor
#
# Tests the color and ambient light sensing abilities of the 
# APDS-9960. Configures APDS-9960 over I2C and polls the sensor for
# ambient light and color levels, which are displayed over the 
# serial console.
# ****************************************************************/


import APDS9960
import streams

streams.serial()


#uint16_t 
ambient_light = 0;
red_light = 0;
green_light = 0;
blue_light = 0;


print("--------------------------------");
print("APDS-9960 - ColorSensor");
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
    blue_light = sensor.readBlueLight()
    
    print("Ambient: ", ambient_light)
    print("Red: ", red_light)
    print("Green: ", green_light)
    print("Blue: ", blue_light)
    
    #Wait 1 second before next reading
    sleep(1000);
