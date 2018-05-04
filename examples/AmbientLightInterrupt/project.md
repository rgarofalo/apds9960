Ambient Light interrupt from APDS-9960
===============================

This example was written from this example of the sparkfun
https://github.com/sparkfun/APDS-9960_RGB_and_Gesture_Sensor

Tests the ambient light interrupt abilities of the APDS-9960.
Configures the APDS-9960 over I2C and waits for an external interrupt based on high or low light conditions. Try covering the sensor with your hand or bringing the sensor close to a bright light source. You might need to adjust the LIGHT_INT_HIGH
and LIGHT_INT_LOW values to get the interrupt to work correctly.
