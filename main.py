# APDS-9960
# Created at 2017-03-15 10:30:00.651123

import streams
import APDS_9960


streams.serial()

sleep(1000)
print("Run Main")

isr_flag = 0

try:
   
    def interruptRoutine():
        print('interruptRoutine')
        isr_flag = 1

    pinMode(D26, INPUT_PULLDOWN)

    sensor = APDS_9960.APDS9960(I2C0)
    sensor.initialize()
    
    if sensor.enableGestureSensor(True):
        print("Gesture sensor is now running")
    else:
        print("Something went wrong during gesture sensor init!")
    

    print('Register')
    print('REG_ENABLE ', sensor.getMode())
    print('REG_GCONF2 ', sensor.getRegGCONF2())
    print('REG_GCONF4 ', sensor.getRegGCONF4())

    onPinFall(D26,interruptRoutine)

    while True:
        print(sensor.getStatus())
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
        sleep(500)
except Exception as e:
    print(e)

