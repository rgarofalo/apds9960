#****************************************************************
# This example was written from this example of the sparkfun
# https://github.com/sparkfun/APDS-9960_RGB_and_Gesture_Sensor
#
# Tests the gesture sensing abilities of the APDS-9960. Configures
# APDS-9960 over I2C and waits for gesture events. Calculates the
# direction of the swipe (up, down, left, right) and displays it
# on a serial console. 
# To perform a NEAR gesture, hold your hand
# far above the sensor and move it close to the sensor (within 2
# inches). Hold your hand there for at least 1 second and move it
# away.
# To perform a FAR gesture, hold your hand within 2 inches of the
# sensor for at least 1 second and then move it above (out of
# range) of the sensor.
#
# ****************************************************************/

import streams
import APDS9960
import threading


streams.serial()
lock= threading.Lock()

flagGesture = threading.Event()
gesture=None
isr_flag=0

def interruptRoutine():
    global isr_flag
    if isr_flag==0:
        isr_flag = 1

onPinFall(D21,interruptRoutine)

print("---------------------------------------")
print("APDS-9960 - Gesture")
print("---------------------------------------")
     

try:
   
    IRGesture = APDS9960.APDS9960(I2C0)
    IRGesture.initialize()
    IRGesture.enableGestureSensor(True)
    

    
except Exception as e:
    print(e)
    
def irGestureRun():
    global isr_flag, IRGesture, gesture, flagGesture
    while True:
        try:
            lock.acquire()
            
            if isr_flag==1:
                if IRGesture.isGestureAvailable():
                    gesture = IRGesture.readGesture()
                    flagGesture.set()
                   
                else:
                    print("Gesture Disable")
                
                isr_flag=0
                
            lock.release()

                
        except Exception as e:
            print(e)
        
        sleep(20)



def gestureRecognition():
    global gesture
    while True:
        lock.acquire()
        
            
        if gesture == 'DIR_UP':
            print("UP")
        elif gesture == 'DIR_DOWN':
            print("DOWN")
        elif gesture =='DIR_LEFT':
            print("LEFT")
        elif gesture == 'DIR_RIGHT':
            print('RIGHT')
        elif gesture == 'DIR_NEAR':
            print('NEAR')
        elif gesture =='DIR_FAR':
            print("FAR")
        else:
            print("NONE")

        lock.release()
        sleep(500)
        flagGesture.wait()
        flagGesture.clear()
    
   
thread(gestureRecognition)
thread(irGestureRun)



           

