
import i2c
import streams

streams.serial()


 # BMP180 default address.
APDS9960_I2CADDR = 0x39

class APDS9960(i2c.I2C):
    
    def __init__(self, i2cdrv, addr=0x39, clk=100000):
        i2c.I2C.__init__(self,i2cdrv,addr,clk)
        self._addr = addr
        self.start()
    
    def get_device_id(self):
        n= self.write_read(0x92, 1)
        return n
