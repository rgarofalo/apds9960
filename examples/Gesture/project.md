Read Gesture from APDS-9960
===============================

This example was written from this example of the sparkfun https://github.com/sparkfun/APDS-9960_RGB_and_Gesture_Sensor

Tests the gesture sensing abilities of the APDS-9960. Configures APDS-9960 over I2C and waits for gesture events. Calculates the direction of the swipe (up, down, left, right) and displays it on a serial console. 
To perform a NEAR gesture, hold your hand far above the sensor and move it close to the sensor (within 2 inches). Hold your hand there for at least 1 second and move it away.
To perform a FAR gesture, hold your hand within 2 inches of the sensor for at least 1 second and then move it above (out of range) of the sensor.
