# APDS-9960
# Created at 2017-03-15 10:30:00.651123

import streams


streams.serial()

sleep(3000)
print("start")

isr_flag =0
try:
    import APDS9960

    def interruptRoutine():
        global isr_flag
        if isr_flag==0:
            isr_flag = 1

    onPinFall(D26,interruptRoutine)
    pinMode(LED1,OUTPUT)
    pinMode(LED2,OUTPUT)
    pinMode(LED3,OUTPUT)
    pinMode(LED4,OUTPUT)

    sensor = APDS9960.APDS9960(I2C0)
    
    id=sensor.get_device_id()
    sensor.initialize()
    

    if sensor.enableGestureSensor(True):
        print("Gesture sensor is now running")
    else:
        print("Something went wrong during gesture sensor init!")
    
    print("device ID: ", hex(id) )
    
    sensor.printReg()
    

    def blink(pin):
        digitalWrite(pin, HIGH)
        sleep(300)
        digitalWrite(pin,LOW)
    
    def blinkAll():
        digitalWrite(LED1, HIGH)
        digitalWrite(LED2, HIGH)
        digitalWrite(LED3, HIGH)
        digitalWrite(LED4, HIGH)

        sleep(300)
        digitalWrite(LED1,LOW)
        digitalWrite(LED2,LOW)
        digitalWrite(LED3,LOW)
        digitalWrite(LED4,LOW)
    
    
        
    while True:
        try:
            if isr_flag==1:
                if sensor.isGestureAvailable():
                    gest = sensor.readGesture()
                    if gest == 'DIR_UP':
                        print("UP")
                        blink(LED2)
                    elif gest == 'DIR_DOWN':
                        print("DOWN")
                        blink(LED4)
                    elif gest =='DIR_LEFT':
                        print("LEFT")
                        blink(LED1)
                    elif gest == 'DIR_RIGHT':
                        print('RIGHT')
                        blink(LED3)
                    elif gest == 'DIR_NEAR':
                        print('NEAR')
                    elif gest =='DIR_FAR':
                        print("FAR")
                    else:
                        print("NONE")
                        blinkAll()
                        
                else:
                    print("Gesture Disable")
                
                isr_flag=0

                
        except Exception as e:
            print(e)
        
        sleep(20)


except Exception as e:
    print(e)

