
import i2c
import streams

streams.serial()


new_exception(RuntimeErrorSet,ValueError,'Cannot override values')
new_exception(RuntimeErrorDel,ValueError,'Cannot delete values')
new_exception(ErrorReadingRegister,RuntimeError,'It was an error while reading the register')
new_exception(ErrorWritingRegister,RuntimeError,'There was an error writing to the register')

 # BMP180 default address.
APDS9960_I2CADDR = 0x39

class gesture_data_type():
    def __init__(self):
        self.u_data = 0
        self.d_data = 0 
        self.l_data = 0
        self.r_data = 0
        self.index = 0
        self.total_gestures = 0
        self.in_threshold = 0
        self.out_threshold = 0


#Direction definitions
direction = enumerate(['DIR_NONE', 'DIR_LEFT', 'DIR_RIGHT', 'DIR_UP', 'DIR_DOWN', 'DIR_NEAR', 'DIR_FAR', 'DIR_ALL'])

class APDS9960(i2c.I2C):
    
    def __init__(self, i2cdrv, addr=0x39, clk=100000):
        i2c.I2C.__init__(self,i2cdrv,addr,clk)
        self._addr = addr
        self.start()
         
        self.gesture_ud_delta_ = 0
        self.gesture_lr_delta_ = 0
    
        self.gesture_ud_count_ = 0
        self.gesture_lr_count_ = 0
    
        self.gesture_near_count_ = 0
        self.gesture_far_count_ = 0
    
        self.gesture_state_ = 0
        self.gesture_motion_ = direction.DIR_NONE
        self.gesture_data_= gesture_data_type()
    
    def get_device_id(self):
        n= self.write_read(0x92, 1)
        return n
