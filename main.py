# APDS-9960
# Created at 2017-03-15 10:30:00.651123

import streams
import APDS_9960

import adc

streams.serial()

sleep(1000)
print("start")

isr_flag = 0

try:
   
    def interruptRoutine():
        print('sd')
        isr_flag = 1

    pinMode(D26, INPUT_PULLDOWN)
    onPinRise(D26,interruptRoutine)

    sensor = APDS_9960.APDS9960(I2C0)
    
    id=sensor.get_device_id()
    sensor.initialize()
    
    
    if sensor.enableGestureSensor(True):
        print("Gesture sensor is now running")
    else:
        print("Something went wrong during gesture sensor init!")
    
    print("device ID: ", id )
    
    while True:
        print(digitalRead(D26))
        if(isr_flag==1):
            if sensor.isGestureAvailable():
                gest = sensor.readGesture()
                if gest == 'DIR_UP':
                    print("UP")
                elif gest== 'DIR_DOWN':
                    print("DOWN")
                elif gest=='DIR_LEFT':
                    print("LEFT")
                elif gest == 'DIR_RIGHT':
                    print('RIGHT')
                elif gest == 'DIR_NEAR':
                    print('NEAR')
                elif gest=='DIR_FAR':
                    print("FAR")
                else:
                    print("NONE")
                    
            else:
                print('Gesture Disable')
            isr_flag=0
        sleep(200)

except Exception as e:
    print(e)

