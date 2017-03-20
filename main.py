# APDS-9960
# Created at 2017-03-15 10:30:00.651123

import streams

streams.serial()

sleep(1000)
print("start")


try:
   
    import apd
    sensor = apd.APDS9960(I2C0)
    print('ok')
    # id=sensor.get_device_id()
    
 
    # sensor.initialize()
    
    
    # print("device ID: ", id )
    # sleep(1000)
    
    
    # while True:
    #     if sensor.isGestureAvailable():
    #          print(sensor.readGesture())
    #     sleep(1000)
except Exception as e:
    print(e)

