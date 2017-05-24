.. module:: APDS9960

*************
APDS9960 Module
*************

This module contains the driver for APDS-9960, It's  features are Gesture detection,  Proximity  detection,  Digital  Ambient  Light  Sense (ALS) and Color Sense (RGBC)
The APDS-9960 is a serious little piece of hardware with built in UV and IR blocking filters, four separate diodes sensitive to different directions, and an I2C compatible interface
(`datasheet <https://cdn.sparkfun.com/datasheets/Sensors/Proximity/apds9960.pdf>`_).
    ==================
    The APDS9960 class
    ==================

.. class:: APDS9960(drivername)
     
.. method:: getMode()

    Reads and returns the contents of the ENABLE register
.. method:: enableLightSensor(interrupts)

    Starts the light (R/G/B/Ambient) sensor on the APDS-9960
    interrupts True to enable hardware interrupt on high or low light
.. method:: disableLightSensor(interrupts)

    Ends the light sensor on the APDS-9960
.. method:: enableProximitySensor(interrupts)

    Starts the proximity sensor on the APDS-9960
    interrupts True to enable hardware external interrupt on proximity
.. method:: disableProximitySensor()

    Ends the proximity sensor on the APDS-9960
.. method:: enableGestureSensor(interrupts)

    Starts the gesture recognition engine on the APDS-9960
    
    Enable gesture mode
    Set ENABLE to 0 (power off)
    Set WTIME to 0xFF
    Set AUX to LED_BOOST_300
    Enable PON, WEN, PEN, GEN in ENABLE
    
    return True if gesture enable. False otherwise.
.. method:: disableGestureSensor()

    Ends the gesture recognition engine on the APDS-9960
    return True if engine disabled correctly. False on error.
.. method:: isGestureAvailable()
    
    Determines if there is a gesture available for reading
    return True if gesture available. False otherwise.
.. method:: readGesture()

    Processes a gesture event and returns best guessed gesture
    return Number corresponding to gesture.
.. method::enablePower()

    Turn the APDS-9960 on
    return True if operation successful. False otherwise.
.. method::disablePower()
    
    Turn the APDS-9960 off
    return True if operation successful. False otherwise.
.. method:.readAmbientLight()

    Reads the ambient (clear) light level as a 16-bit value
    return value of the light sensor.
.. method:: setLEDDrive(drive)

    brief Sets the LED drive strength for proximity and ALS
     
        Value    LED Current
          0        100 mA
          1         50 mA
          2         25 mA
          3         12.5 mA
     
     drive the value (0-3) for the LED drive strength
     
.. method:: getProximityGain()

    Returns receiver gain for proximity detection
     
      Value    Gain
        0       1x
        1       2x
        2       4x
        3       8x
     
      return the value of the proximity gain.
.. method:: setProximityGain(drive):

    Sets the receiver gain for proximity detection
    
     Value    Gain
       0       1x
       1       2x
       2       4x
       3       8x
    
    drive the value (0-3) for the gain
    return True if operation successful.
.. method:: getAmbientLightGain()

    Returns receiver gain for the ambient light sensor (ALS)
 
        Value    Gain
          0        1x
          1        4x
          2       16x
          3       64x

    return the value of the ALS gain. 0xFF on failure.
.. method:: setAmbientLightGain(drive)

    Sets the receiver gain for the ambient light sensor (ALS)
 
      Value    Gain
        0        1x
        1        4x
        2       16x
        3       64x
     
    drive the value (0-3) for the gain
    return True if operation successful. False otherwise.
.. method:: getLEDBoost()

    brief Get the current LED boost value
    Value  Boost Current
      0        100%
      1        150%
      2        200%
      3        300%
 
     return the LED boost value.
.. method:: getGestureGain()

    Gets the gain of the photodiode during gesture mode
    
      Value    Gain
        0       1x
        1       2x
        2       4x
        3       8x
        
    return the current photodiode gain.
.. method:: setGestureGain(gain)

    Sets the gain of the photodiode during gesture mode
 
        Value    Gain
          0       1x
          1       2x
          2       4x
          3       8x
 
    gain the value for the photodiode gain
.. method:: getGestureLEDDrive()

    Gets the drive current of the LED during gesture mode
 
      Value    LED Current
        0        100 mA
        1         50 mA
        2         25 mA
        3         12.5 mA
 
   return the LED drive current value.
.. method:: setGestureLEDDrive(drive)
    
    Sets the LED drive current during gesture mode
 
        Value    LED Current
          0        100 mA
          1         50 mA
          2         25 mA
          3         12.5 mA
 
    drive the value for the LED drive current
.. method: getGestureWaitTime
    Gets the time in low power mode between gesture detections
 
        Value    Wait time
          0          0 ms
          1          2.8 ms
          2          5.6 ms
          3          8.4 ms
          4         14.0 ms
          5         22.4 ms
          6         30.8 ms
          7         39.2 ms
 
    return the current wait time between gestures.
.. method:: setGestureWaitTime(time)
    Sets the time in low power mode between gesture detections
 
        Value    Wait time
          0          0 ms
          1          2.8 ms
          2          5.6 ms
          3          8.4 ms
          4         14.0 ms
          5         22.4 ms
          6         30.8 ms
          7         39.2 ms
 
    the value for the wait time
.. method:: setLightIntLowThreshold(threshold)

    Sets the low threshold for ambient light interrupts
    threshold low threshold value for interrupt to trigger
.. method:: setLightIntHighThreshold(threshold)
    
    Sets the low threshold for ambient light interrupts
    threshold low threshold value for interrupt to trigger
.. method:: setAmbientLightIntEnable(enable)
    
    Turns ambient light interrupts on or off

    enable 1 to enable interrupts, 0 to turn them off
    return True if operation successful. False otherwise.
.. method:: setProximityIntEnable(enable)

    Turns proximity interrupts on or off
    enable 1 to enable interrupts, 0 to turn them off
    return True if operation successful. False otherwise.
.. method:: getGestureIntEnable()

    Gets if gesture interrupts are enabled or not
    return 1 if interrupts are enabled, 0 if not.
.. method:: setGestureIntEnable(enable)

    Turns gesture-related interrupts on or off
    enable 1 to enable interrupts, 0 to turn them off
    return True if operation successful.
.. method:: setGestureMode(mode)

    Tells the state machine to either enter or exit gesture state machine
    mode 1 to enter gesture state machine, 0 to exit.
    True if operation successful. False otherwise.
