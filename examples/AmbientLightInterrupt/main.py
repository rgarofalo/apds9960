# /****************************************************************


#****************************************************************/

import APDS9960
import streams

streams.serial()

APDS9960_INT = D21  #Needs to be an interrupt pin
LED_PIN = LED1 #LED for showing interrupt

LIGHT_INT_HIGH = 1000 #High light level for interrupt
LIGHT_INT_LOW  = 10   #Low light level for interrupt

ambient_light = 0
red_light = 0
green_light = 0
blue_light = 0

isr_flag=0
threshold = 0

print("-------------------------------------")
print("APDS-9960 - Light Interrupts")
print("-------------------------------------")
  

def interruptRoutine():
    global isr_flag
    if isr_flag==0:
        isr_flag = 1


onPinRise(APDS9960_INT,interruptRoutine)
pinMode(LED_PIN,OUTPUT)




#Initialize APDS-9960 (configure I2C and initial values)
try:
    
    sensor = APDS9960.APDS9960(I2C0)
    sensor.initialize()
    print("APDS-9960 initialization complete")
    
except:
    print("Something went wrong during APDS-9960 init!")

try:
    #Set high and low interrupt thresholds
    sensor.setLightIntLowThreshold(LIGHT_INT_LOW)
except:
    print("Error writing low threshold")

try:
    sensor.setLightIntHighThreshold(LIGHT_INT_HIGH)
except:
    print("Error writing high threshold")

try:
#Start running the APDS-9960 light sensor (no interrupts)
    sensor.enableLightSensor(False)
    print("Light sensor is now running")
except:
    print("Something went wrong during light sensor init!")
  
try:
    #Read high and low interrupt thresholds
    sensor.getLightIntLowThreshold(threshold)
    print("Low Threshold:" , threshold)

except:
    print("Error reading low threshold")

    
try:
    sensor.getLightIntHighThreshold(threshold)
    print("High Threshold:",threshold)
except:
    print("Error reading high threshold")


try:
    #Enable interrupts
    sensor.setAmbientLightIntEnable(1)
except:
    print("Error enabling interrupts")

  
#Wait for initialization and calibration to finish
sleep(500)

while True:
  #If interrupt occurs, print out the light levels
  if isr_flag == 1:
    
    ambient_light = sensor.readAmbientLight()
    red_light = sensor.readRedLight() 
    green_light = sensor.readGreenLight()
    blue_light = sensor.readBlueLight()
    #Read the light levels (ambient, red, green, blue) and print
    print("Interrupt! Ambient:", ambient_light)
    print("R:", red_light)
    print("G:",green_light)
    print("B:",blue_light)
    
    #Turn on LED for a half a second
    digitalWrite(LED_PIN, HIGH)
    sleep(500)
    digitalWrite(LED_PIN, LOW)
    
    #Reset flag and clear APDS-9960 interrupt (IMPORTANT!)
    isr_flag = 0
    sensor.clearAmbientLightInt()

    