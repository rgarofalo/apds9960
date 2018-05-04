#****************************************************************
# This example was written from this example of the sparkfun
# https://github.com/sparkfun/APDS-9960_RGB_and_Gesture_Sensor
#
# Tests the proximity sensing abilities of the APDS-9960.
# Configures the APDS-9960 over I2C and polls for the distance to
# the object nearest the sensor.
#
#****************************************************************/

import streams
streams.serial()
sleep(3000)

import APDS9960

proximity_data       = 0  
PGAIN_2X             = 1


print("------------------------------------")
print("APDS-9960 - ProximitySensor")
print("------------------------------------")
  
# Initialize APDS-9960 (configure I2C and initial values)
sensor = APDS9960.APDS9960(I2C0)
sensor.initialize()
print("APDS-9960 initialization complete")

try:
    sensor.setProximityGain(PGAIN_2X)
except:
    print("Something went wrong trying to set PGAIN")


#Start running the APDS-9960 proximity sensor (no interrupts)
sensor.enableProximitySensor(False)
print"Proximity sensor is now running")

while(True):
    proximity_data = sensor.readProximity()

    print("Proximity: ", proximity_data);
    
    #Wait 250 ms before next reading
    sleep(250)
  