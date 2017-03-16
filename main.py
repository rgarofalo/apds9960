# APDS-9960
# Created at 2017-03-15 10:30:00.651123


import streams

streams.serial()

sleep(1000)
print("start")
while True:
    try:
        import APDS_9960
        sensor = APDS_9960.APDS9960(I2C0)
        #print("device ID: {:#X}".format(sensor.get_device_id()))
        sensor.initialize()
    except Exception as e:
        print(e)
    sleep(1000)
print ("Start")
while True:
    print(sensor.gesture())
    sleep(1000)