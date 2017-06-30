.. module:: Avago.APDS9960

*************
APDS9960 Module
*************

This module contains the driver for APDS-9960, It's  features are Gesture detection,  Proximity  detection,  Digital  Ambient  Light  Sense (ALS) and Color Sense (RGBC).

The APDS-9960 is a serious little piece of hardware with built in UV and IR blocking filters, four separate diodes sensitive to different directions, and an I2C compatible interface
(`datasheet <https://cdn.sparkfun.com/datasheets/Sensors/Proximity/apds9960.pdf>`_).
    ==================
    The APDS9960 class
    ==================

.. class:: APDS9960(drivername)
     
.. method:: getMode()

    Reads and returns the contents of the ENABLE register
.. method:: setMode(mode, enable)

    Enables or disables a feature in the APDS-9960
    
    mode: 
        feature to enable  
    
    enable:
        ON (1) or OFF (0)
.. method:: enableLightSensor(interrupts)

    Starts the light (R/G/B/Ambient) sensor on the APDS-9960
    
    interrupts:
        True to enable hardware interrupt on high or low light
.. method:: disableLightSensor()

    Ends the light sensor on the APDS-9960
.. method:: enableProximitySensor(interrupts)

    Starts the proximity sensor on the APDS-9960
    
    interrupts:
        True to enable hardware external interrupt on proximity
.. method:: disableProximitySensor()

    Ends the proximity sensor on the APDS-9960
.. method:: enableGestureSensor(interrupts)

    Starts the gesture recognition engine on the APDS-9960
    
    * Enable gesture mode
    * Set ENABLE to 0 (power off)
    * Set WTIME to 0xFF
    * Set AUX to LED_BOOST_300
    * Enable PON, WEN, PEN, GEN in ENABLE
.. method:: disableGestureSensor()

    Ends the gesture recognition engine on the APDS-9960
.. method:: isGestureAvailable()
    
    Determines if there is a gesture available for reading
    
    return:
        True if gesture available. False otherwise.
.. method:: readGesture()

    Processes a gesture event and returns best guessed gesture
    
    return:
        Number corresponding to gesture.
.. method::enablePower()

    Turn the APDS-9960 on
    
.. method::disablePower()
    
    Turn the APDS-9960 off
.. method:: readAmbientLight()

    Reads the ambient (clear) light level as a 16-bit value
    
    return:
        the value of the light sensor.
.. method:: readRedLight()
    
    Reads the red light level as a 16-bit value
    
    return:
        the value of the light sensor.
.. method:: readGreenLight()
    
    Reads the red light level as a 16-bit value
    
    return:
        the value of the light sensor.
.. method:: readBlueLight()
    
    Reads the red light level as a 16-bit value
    
    return:
        the value of the light sensor.
.. method:: readProximity()

    Reads the proximity level as an 8-bit value
    
    return:
        the value of the proximity sensor.
.. method:: getProxIntLowThresh()

    Returns the lower threshold for proximity detection
.. method:: getProxIntLowThresh(threshold)
    
    Sets the lower threshold for proximity detection
.. method:: getProxIntHighThresh()

    Returns the high threshold for proximity detection
.. method:: setProxIntHighThresh(threshold)

    Sets the high threshold for proximity detection
.. method:: getLEDDrive()
    
    Returns LED drive strength for proximity and ALS
    
    +---------+---------------+
    |  Value  |  LED Current  |
    +---------+---------------+
    |    0    |    100 mA     |
    +---------+---------------+
    |    1    |     50 mA     |
    +---------+---------------+
    |    2    |     25 mA     |
    +---------+---------------+
    |    3    |     12.5 mA   |
    +---------+---------------+
    
.. method:: setLEDDrive(drive)
    
    brief Sets the LED drive strength for proximity and ALS
    
    drive:
        the value (0-3) for the LED drive strength
     
    +---------+---------------+
    |  Value  |  LED Current  |
    +---------+---------------+
    |    0    |    100 mA     |
    +---------+---------------+
    |    1    |     50 mA     |
    +---------+---------------+
    |    2    |     25 mA     |
    +---------+---------------+
    |    3    |     12.5 mA   |
    +---------+---------------+
     
     
     
.. method:: getProximityGain()

    Get the gain for proximity detection
    
    return:
        the value of the proximity gain.

     
    +--------+---------+
    |  Value |  Gain   |
    +========+=========+
    |    0   |    1x   |
    +--------+---------+
    |    1   |    2x   |
    +--------+---------+
    |    2   |    4x   |
    +--------+---------+
    |    3   |    8x   |
    +--------+---------+
     
.. method:: setProximityGain(drive):

    Sets the receiver gain for proximity detection
    
    drive:
        the value (0-3) for the gain
     
    +--------+---------+
    |  Value |  Gain   |
    +========+=========+
    |    0   |    1x   |
    +--------+---------+
    |    1   |    2x   |
    +--------+---------+
    |    2   |    4x   |
    +--------+---------+
    |    3   |    8x   |
    +--------+---------+
    
.. method:: getAmbientLightGain()

    Get the gain for the ambient light sensor (ALS)
    
    return:
        the value of the ALS gain.


    +--------+---------+
    |  Value |  Gain   |
    +========+=========+
    |    0   |    1x   |
    +--------+---------+
    |    1   |    4x   |
    +--------+---------+
    |    2   |    16x  |
    +--------+---------+
    |    3   |    64x  |
    +--------+---------+
    
.. method:: setAmbientLightGain(drive)

    Sets the receiver gain for the ambient light sensor (ALS)
    
    drive:
        the value (0-3) for the gain
    
    return:
        True if operation successful.


    +--------+---------+
    |  Value |  Gain   |
    +========+=========+
    |    0   |    1x   |
    +--------+---------+
    |    1   |    4x   |
    +--------+---------+
    |    2   |    16x  |
    +--------+---------+
    |    3   |    64x  |
    +--------+---------+
    
     
    
.. method:: getLEDBoost()

    Get the current LED boost value
    
    return:
        the LED boost value.
    
    +-------+----------------+
    | Value | Boost Current  |
    +=======+================+
    |  0    |  100%          |
    +-------+----------------+
    |  1    |  150%          |
    +-------+----------------+
    |  2    |  200%          |
    +-------+----------------+
    |  3    |  300%          |
    +-------+----------------+
    
      
      
.. method:: setLEDBoost(boost)
.. method:: getProxGainCompEnable()
    
    Gets proximity gain compensation enable
    
    return:
        1 if compensation is enabled or 0 if not. 
.. method:: setProxGainCompEnable(enable)
    
    Sets the proximity gain compensation enable.
    
    enable:
        1 to enable compensation or  0 to disable compensation.
.. method:: getProxPhotoMask()

    Gets the current mask for enabled/disabled proximity photodiodes
    
    1 = disabled, 0 = enabled
    
    +-----+-----------------+
    | Bit |   Photodiode    |
    +=====+=================+
    | 3   |    UP           |
    +-----+-----------------+
    | 2   |    DOWN         |
    +-----+-----------------+
    | 1   |    LEFT         |
    +-----+-----------------+
    | 0   |    RIGHT        |
    +-----+-----------------+
.. method:: setProxPhotoMask(mask)

    Sets the mask for enabling/disabling proximity photodiodes
    
    1 = disabled, 0 = enabled
    
    +-----+-----------------+
    | Bit |   Photodiode    |
    +=====+=================+
    | 3   |    UP           |
    +-----+-----------------+
    | 2   |    DOWN         |
    +-----+-----------------+
    | 1   |    LEFT         |
    +-----+-----------------+
    | 0   |    RIGHT        |
    +-----+-----------------+
.. method:: getGestureEnterThresh()
    
    Gets the entry proximity threshold for gesture sensing
.. method:: setGestureEnterThresh(threshold)
    
    Sets the entry proximity threshold for gesture sensing
    
    threshold: 
        the proximity value needed to start gesture mode
    
.. method:: getGestureExitThresh()
    
    Gets the exit proximity threshold for gesture sensing
.. method:: setGestureExitThresh(threshold)
    
    Sets the exit proximity threshold for gesture sensing
    
    threshold:
        the proximity value needed to end gesture mode
    
    
.. method:: getGestureGain()

    Gets the gain of the photodiode during gesture mode
    
    return:
        the value for the current photodiode gain.
    
        +--------+----------+
        | Value  |  Gain    |
        +========+==========+
        |  0     |  1x      |
        +--------+----------+
        |  1     |  2x      |
        +--------+----------+
        |  2     |  4x      |
        +--------+----------+
        |  3     |  8x      |
        +--------+----------+
        
    
.. method:: setGestureGain(value)

    Sets the gain of the photodiode during gesture mode
    
    value:
        the value for the gain of the gesture
        
 
    +--------+----------+
    | Value  |  Gain    |
    +========+==========+
    |  0     |  1x      |
    +--------+----------+
    |  1     |  2x      |
    +--------+----------+
    |  2     |  4x      |
    +--------+----------+
    |  3     |  8x      |
    +--------+----------+
.. method:: getGestureLEDDrive()

    Gets the drive current of the LED during gesture mode
    
    return:
        the LED drive current value.

 
    +--------+--------------+
    | Value  |  LED Current |
    +========+==============+
    |  0     |   100 mA     |
    +--------+--------------+
    |  1     |    50 mA     |
    +--------+--------------+
    |  2     |    25 mA     |
    +--------+--------------+
    |  3     |    12.5 mA   |
    +--------+--------------+

 
.. method:: setGestureLEDDrive(drive)

    Sets the LED drive current during gesture mode
    
    drive:
        the value for the LED drive current
    
    +--------+--------------+
    | Value  |  LED Current |
    +========+==============+
    |  0     |   100 mA     |
    +--------+--------------+
    |  1     |    50 mA     |
    +--------+--------------+
    |  2     |    25 mA     |
    +--------+--------------+
    |  3     |    12.5 mA   |
    +--------+--------------+


 
    
.. method: getGestureWaitTime
    Gets the time in low power mode between gesture detections
    
    return:
        the current wait time between gestures.

 
    +----------+-------------+
    |  Value   |  Wait time  |
    +==========+=============+
    |    0     |     0 ms    |
    +----------+-------------+
    |    1     |     2.8 ms  |
    +----------+-------------+
    |    2     |     5.6 ms  |
    +----------+-------------+
    |    3     |     8.4 ms  |
    +----------+-------------+
    |    4     |    14.0 ms  |
    +----------+-------------+
    |    5     |    22.4 ms  |
    +----------+-------------+
    |    6     |    30.8 ms  |
    +----------+-------------+
    |    7     |    39.2 ms  |
    +----------+-------------+
 
.. method:: setGestureWaitTime(time)

    Sets the time in low power mode between gesture detections
    
    time:
        the value for the wait time

    +----------+-------------+
    |  Value   |  Wait time  |
    +==========+=============+
    |    0     |     0 ms    |
    +----------+-------------+
    |    1     |     2.8 ms  |
    +----------+-------------+
    |    2     |     5.6 ms  |
    +----------+-------------+
    |    3     |     8.4 ms  |
    +----------+-------------+
    |    4     |    14.0 ms  |
    +----------+-------------+
    |    5     |    22.4 ms  |
    +----------+-------------+
    |    6     |    30.8 ms  |
    +----------+-------------+
    |    7     |    39.2 ms  |
    +----------+-------------+
 
.. method:: getLightIntLowThreshold()
    
    Gets the low threshold for ambient light interrupts
    
    Return:
        the current low threshold stored on the APDS-9960
    
.. method:: setLightIntLowThreshold(threshold)

    Sets the low threshold for ambient light interrupts
    
    threshold:
        the low threshold value for interrupt to trigger
.. method:: getLightIntHighThreshold()

    Gets the high threshold for ambient light interrupts
    
    return: 
        the current hight threshold stored on the APDS-9960
.. method:: setLightIntHighThreshold(threshold)
    
    Sets the hight threshold for ambient light interrupts
    
    threshold:
        the hight threshold value for interrupt to trigger
.. method:: getProximityIntLowThreshold()
    
    Gets the low threshold for proximity interrupts
.. method:: setProximityIntLowThreshold(threshold)

    Sets the low threshold for proximity interrupts
    
    threshold:
        the low threshold value for interrupt to trigger
.. method:: getProximityIntHighThreshold()
    
   Gets the high threshold for proximity interrupts
.. method:: setProximityIntHighThreshold(threshold)
    
    Sets the high threshold for proximity interrupts
    
    threshold: 
        the high threshold value for interrupt to trigger
.. method:: getAmbientLightIntEnable()
    
    Gets if ambient light interrupts are enabled or not
    
    Return:
        1 if interrupts are enabled, 0 if not.
.. method:: setAmbientLightIntEnable(enable)
    
    Turns ambient light interrupts on or off
    
    enable:
        1 to enable interrupts or 0 to turn them off
.. method:: getProximityIntEnable()
    
    Gets if proximity interrupts are enabled or not
    
    Return:
        1 if interrupts are enabled or 0 if not.
.. method:: setProximityIntEnable(enable)

    Turns proximity interrupts on or off
    
    enable:
        1 to enable interrupts or 0 to turn them off
.. method:: getGestureIntEnable()

    Gets if gesture interrupts are enabled or not
    
    return:
        1 if interrupts are enabled or 0 if not.
.. method:: setGestureIntEnable(enable)

    Turns gesture-related interrupts on or off
    
    enable:
        1 to enable interrupts or 0 to turn them off
.. method:: clearAmbientLightInt()

    Clears the ambient light interrupt
.. method:: clearProximityInt()

    Clears the proximity interrupt
    
.. method:: getGestureMode()

    Tells if the gesture state machine is currently running
    
    return:
        1 if gesture state machine is running or 0 if not
.. method:: setGestureMode(mode)

    Tells the state machine to either enter or exit gesture state machine
    
    mode:
        1 to enter gesture state machine or 0 to exit.
    
