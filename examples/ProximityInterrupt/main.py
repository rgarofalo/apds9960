#****************************************************************

#
# ****************************************************************/


import streams
streams.serial()
sleep(3000)

import APDS9960

APDS9960_INT    = D21  #Needs to be an interrupt pin
LED_PIN         = LED1 # LED for showing interrupt

#Constants
PROX_INT_HIGH   =  50  #Proximity level for interrupt
PROX_INT_LOW    = 0 #No far interrupt
PGAIN_2X        =   1

#Global variables

proximity_data = 0;
isr_flag = 0;

def interruptRoutine():
    global isr_flag
    if isr_flag==0:
        isr_flag = 1

onPinRise(APDS9960_INT,interruptRoutine)
pinMode(LED_PIN,OUTPUT)

print("---------------------------------------")
print("APDS-9960 - ProximityInterrupt")
print("---------------------------------------")
  
# Initialize APDS-9960 (configure I2C and initial values)
sensor = APDS9960.APDS9960(I2C0)
sensor.initialize()
print("APDS-9960 initialization complete")

sensor.setProximityGain(PGAIN_2X)
print("Something went wrong trying to set PGAIN")

#Set proximity interrupt thresholds
try:
    sensor.setProximityIntLowThreshold(PROX_INT_LOW)
except:
    print("Error writing low threshold")

try:
    sensor.setProximityIntHighThreshold(PROX_INT_HIGH)
except:
    print("Error writing high threshold")

#Start running the APDS-9960 proximity sensor (interrupts)
try:
    sensor.enableProximitySensor(True)
except:
    print("Proximity sensor is now running")

while True:
    if isr_flag==1: #If interrupt occurs, print out the proximity level
        proximity_data = sensor.readProximity()
        print("Proximity detected! Level: ", proximity_data)
        
        #Turn on LED for a half a second
        digitalWrite(LED_PIN, HIGH)
        sleep(500)
        digitalWrite(LED_PIN, LOW)
        #Reset flag and clear APDS-9960 interrupt (IMPORTANT!)
        isr_flag = 0
        sensor.clearProximityInt()