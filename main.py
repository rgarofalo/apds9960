# APDS-9960
# Created at 2017-03-15 10:30:00.651123

import streams

streams.serial()

sleep(1000)
print("start")


try:
    import APDS_9960
    sensor = APDS_9960.APDS9960(I2C0)
    print('ok')
    id=sensor.get_device_id()
    
 
    sensor.initialize()
    
    
    print("device ID: ", id )
    sleep(1000)
    
    
    while True:
        print(sensor.gesture())
        sleep(1000)
except Exception as e:
    print(e)

