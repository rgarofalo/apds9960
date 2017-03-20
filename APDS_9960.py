"""
.. module:: APDS9960

*************
APDS9960 Module
*************

This module contains the driver for APDS-9960, It's  features are Gesture detection,  Proximity  detection,  Digital  Ambient  Light  Sense (ALS) and Color Sense (RGBC)
The APDS-9960 is a serious little piece of hardware with built in UV and IR blocking filters, four separate diodes sensitive to different directions, and an I2C compatible interface
(`datasheet <https://cdn.sparkfun.com/datasheets/Sensors/Proximity/apds9960.pdf>`_).
"""


import i2c
import streams

streams.serial()


# BMP180 default address.
APDS9960_I2CADDR = 0x39
# Register addresses
REG_ENABLE  = 0x80
REG_ATIME   = 0x81
REG_WTIME   = 0x83
REG_AILTL   = 0x84
REG_AILTH   = 0x85
REG_AIHTL   = 0x86
REG_AIHTH   = 0x87
REG_PILT    = 0x89
REG_PIHT    = 0x8B
REG_PERS    = 0x8C
REG_CONFIG1 = 0x8D
REG_PPULSE  = 0x8E
REG_CONTROL = 0x8F
REG_CONFIG2 = 0x90
REG_ID = 0x92
REG_STATUS  = 0x93
REG_CDATAL  = 0x94
REG_CDATAH  = 0x95
REG_RDATAL  = 0x96
REG_RDATAH  = 0x97
REG_GDATAL  = 0x98
REG_GDATAH  = 0x99
REG_BDATAL  = 0x9A
REG_BDATAH  = 0x9B
REG_PDATA   = 0x9C
REG_POFFSET_UR  = 0x9D
REG_POFFSET_DL  = 0x9E
REG_CONFIG3 = 0x9F
REG_GPENTH  = 0xA0
REG_GEXTH   = 0xA1
REG_GCONF1  = 0xA2
REG_GCONF2  = 0xA3
REG_GOFFSET_U   = 0xA4
REG_GOFFSET_D   = 0xA5
REG_GOFFSET_L   = 0xA7
REG_GOFFSET_R   = 0xA9
REG_GPULSE  = 0xA6
REG_GCONF3  = 0xAA
REG_GCONF4  = 0xAB
REG_GFLVL   = 0xAE
REG_GSTATUS = 0xAF
REG_IFORCE  = 0xE4
REG_PICLEAR = 0xE5
REG_CICLEAR = 0xE6
REG_AICLEAR = 0xE7
REG_GFIFO_U = 0xFC
REG_GFIFO_D = 0xFD
REG_GFIFO_L = 0xFE
REG_GFIFO_R = 0xFF

# Enable register bits
ENABLE_GEN  = 0b01000000    # Gesture enable
ENABLE_PIEN = 0b00100000    # Proximity Interrupt Enable
ENABLE_AIEN = 0b00010000    # ALS Interrupt Enable
ENABLE_WEN  = 0b00001000    # Wait Enable
ENABLE_PEN  = 0b00000100    # Proximity Enable
ENABLE_AEN  = 0b00000010    # ALS Enable
ENABLE_PON  = 0b00000001    # Power ON

APDS9960_GVALID  = 0b00000001

#Acceptable parameters for setMode
ENABLE_POWER                 = 0
ENABLE_AMBIENT_LIGHT         = 1
ENABLE_PROXIMITY             = 2
ENABLE_WAIT                  = 3
ENABLE_AMBIENT_LIGHT_INT     = 4
ENABLE_PROXIMITY_INT         = 5
ENABLE_GESTURE               = 6
ENABLE_ALL                   = 7

ENABLE_OFF                   = 0
ENABLE_ON                    = 1



# Congiguration register 2
#LED Boost values
LED_BOOST_100          = 0
LED_BOOST_150          = 1
LED_BOOST_200          = 2
LED_BOOST_300          = 3 

GCONFIG3_GDIMS_LR = 2
GCONFIG3_GDIMS_UD = 1 # 01
GCONFIG4_GMODE = 1 # Gesture mode

#LED Drive values
LED_DRIVE_100MA         = 0
LED_DRIVE_50MA          = 1
LED_DRIVE_25MA          = 2
LED_DRIVE_12_5MA        = 3

# Proximity Gain (PGAIN) values 
PGAIN_1X                = 0
PGAIN_2X                = 1
PGAIN_4X                = 2
PGAIN_8X                = 3

#ALS Gain (AGAIN) values
AGAIN_1X                = 0
AGAIN_4X                = 1
AGAIN_16X               = 2
AGAIN_64X               = 3

#Gesture Gain (GGAIN) values
GGAIN_1X                = 0
GGAIN_2X                = 1
GGAIN_4X                = 2
GGAIN_8X                = 3
 
#Gesture wait time values
GWTIME_0MS              = 0
GWTIME_2_8MS            = 1
GWTIME_5_6MS            = 2
GWTIME_8_4MS            = 3
GWTIME_14_0MS           = 4
GWTIME_22_4MS           = 5
GWTIME_30_8MS           = 6
GWTIME_39_2MS           = 7


#Default values
DEFAULT_ATIME           = 219     # 103ms
DEFAULT_WTIME           = 246     # 27ms
DEFAULT_PROX_PPULSE     = 0x87    # 16us, 8 pulses
DEFAULT_GESTURE_PPULSE  = 0x89    # 16us, 10 pulses
DEFAULT_POFFSET_UR      = 0       # 0 offset
DEFAULT_POFFSET_DL      = 0       # 0 offset      
DEFAULT_CONFIG1         = 0x60    # No 12x wait (WTIME) factor
DEFAULT_LDRIVE          = LED_DRIVE_100MA
DEFAULT_PGAIN           = PGAIN_4X
DEFAULT_AGAIN           = AGAIN_4X
DEFAULT_PILT            = 0       # Low proximity threshold
DEFAULT_PIHT            = 50      # High proximity threshold
DEFAULT_AILT            = 0xFFFF  # Force interrupt for calibration
DEFAULT_AIHT            = 0
DEFAULT_PERS            = 0x11    # 2 consecutive prox or ALS for int.
DEFAULT_CONFIG2         = 0x01    # No saturation interrupts or LED boost  
DEFAULT_CONFIG3         = 0       # Enable all photodiodes, no SAI
DEFAULT_GPENTH          = 40      # Threshold for entering gesture mode
DEFAULT_GEXTH           = 30      # Threshold for exiting gesture mode    
DEFAULT_GCONF1          = 0x40    # 4 gesture events for int., 1 for exit
DEFAULT_GGAIN           = GGAIN_4X
DEFAULT_GLDRIVE         = LED_DRIVE_100MA
DEFAULT_GWTIME          = GWTIME_2_8MS
DEFAULT_GOFFSET         = 0       # No offset scaling for gesture mode
DEFAULT_GPULSE          = 0xC9    # 32us, 10 pulses
DEFAULT_GCONF3          = 0       # All photodiodes active during gesture
DEFAULT_GIEN            = 0       # Disable gesture interrupts


ERROR = 0xFF

DEBUG = 1

class Enumeration(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError
    def __setattr__(self, name, value):
        raise RuntimeErrorSet
    def __delattr__(self, name):
        raise RuntimeErrorDel


#Direction definitions
direction = Enumeration([ 'DIR_NONE', 'DIR_LEFT', 'DIR_RIGHT', 'DIR_UP', 'DIR_DOWN', 'DIR_NEAR', 'DIR_FAR', 'DIR_ALL'])

#State definitions */
state = Enumeration([ 'NA_STATE', 'NEAR_STATE', 'FAR_STATE', 'ALL_STATE'])

#Container for gesture data */
#class gesture_data_type():
#    __slots__=['u_data','d_data','l_data','r_data','index','total_gestures','in_threshold','out_threshold']

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


class APDS9960(i2c.I2C):
    
    def __init__(self, i2cdrv, addr=0x39, clk=100000):
        try:
            print('me')
            i2c.I2C.__init__(self,i2cdrv,addr,clk)
            print('ok2')
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
        except Exception as e:
            print(e)

     
    def _write(self, reg, data):
        buffer = bytearray(1)
        buffer[0] = reg
        buffer.append(data)
        
        self.write(buffer)
 
    def initialize(self):

        if (self.get_device_id()!= 0xAB):
            return False
        
        #Set ENABLE register to 0 (disable all features)
        self.setMode(ENABLE_ALL,ENABLE_OFF)

        self.initiGesture()
       
        #self.write_bytes(REG_CONFIG3, DEFAULT_GCONF3)
        #self.write_bytes(REG_GCONFIG4, GCONFIG4_GMODE)
 
    def initiGesture(self):
        #Set default values for gesture sense registers */
        self.write_bytes(self.REG_GPENTH, self.DEFAULT_GPENTH)
        
        self.write_bytes(self.REG_GEXTH ,self.DEFAULT_GEXTH)
        self.write_bytes(self.REG_GCONF1, self.DEFAULT_GCONF1)
        
        self.write_bytes(REG_GCONF1, DEFAULT_GGAIN)
        self.write_bytes(REG_GCONF1, DEFAULT_GCONF1)
        self.write_bytes(REG_GCONF1, DEFAULT_GCONF1)
        self.write_bytes(REG_GCONF1, DEFAULT_GCONF1)
        self.write_bytes(REG_GCONF1, DEFAULT_GCONF1)

  
        self.setGestureGain(self.DEFAULT_GGAIN)

        self.setGestureLEDDrive(self.DEFAULT_GLDRIVE)
        self.setGestureWaitTime(self.DEFAULT_GWTIME)
    
        self.write_bytes(self.REG_GOFFSET_U, self.DEFAULT_GOFFSET)
     
        self.write_bytes(self.REG_GOFFSET_D, self.DEFAULT_GOFFSET)
     
        self.write_bytes(self.REG_GOFFSET_L, self.DEFAULT_GOFFSET)
    
        self.write_bytes(self.REG_GOFFSET_R, self.DEFAULT_GOFFSET)
      
        self.write_bytes(self.REG_GPULSE, self.DEFAULT_GPULSE) 
        self.write_bytes(self.REG_GCONF3, self.DEFAULT_GCONF3) 
        #         return false;
        #     }
        #     if( !setGestureIntEnable(DEFAULT_GIEN) ) {
        #         return false;
        # }


    def getGestureLEDDrive(self):
        """
            Gets the drive current of the LED during gesture mode
         
              Value    LED Current
                0        100 mA
                1         50 mA
                2         25 mA
                3         12.5 mA
         
           return the LED drive current value. 0xFF on error.
        """
        
        try:
            val = self.write_read(self.REG_GCONF2, 1)
        except:
            raise ErrorReadingRegister
        
        #Shift and mask out GLDRIVE bits */
        val = (val >> 3) & 0b00000011
    
        return val
        
    def setGestureLEDDrive(self, drive):
        """
            Sets the LED drive current during gesture mode
         
                Value    LED Current
                  0        100 mA
                  1         50 mA
                  2         25 mA
                  3         12.5 mA
         
            drive the value for the LED drive current
            return True if operation successful. False otherwise.
        """
        try:
            val = self.write_read(self.REG_GCONF2, 1)
        except:
            raise ErrorReadingRegister
        
    
        #Set bits in register to given value */
        drive &= 0b00000011
        drive = drive << 3
        val &= 0b11100111
        val |= drive
        
          #Write register value back into GCONF2 register
        try:       
            self.write_bytes(self.REG_GCONF2,val)
        except:
           raise ErrorWritingRegister


    def getGestureWaitTime(self):
        """
            Gets the time in low power mode between gesture detections
         
                Value    Wait time
                  0          0 ms
                  1          2.8 ms
                  2          5.6 ms
                  3          8.4 ms
                  4         14.0 ms
                  5         22.4 ms
                  6         30.8 ms
                  7         39.2 ms
         
            return the current wait time between gestures. 0xFF on error.
        """
        try:
            val = self.write_read(self.REG_GCONF2, 1)
        except:
            raise ErrorReadingRegister
    
        #Mask out GWTIME bits */
        val &= 0b00000111
    
        return val


    def setGestureWaitTime(self, time):
        """
            Sets the time in low power mode between gesture detections
         
                Value    Wait time
                  0          0 ms
                  1          2.8 ms
                  2          5.6 ms
                  3          8.4 ms
                  4         14.0 ms
                  5         22.4 ms
                  6         30.8 ms
                  7         39.2 ms
         
            the value for the wait time
            return True if operation successful. False otherwise.
        """

        try:
            val = self.write_read(self.REG_GCONF2, 1)
        except:
            raise ErrorReadingRegister
    
        #Set bits in register to given value */
        time &= 0b00000111
        val &= 0b11111000
        val |= time
    
        try:       
            self.write_bytes(self.REG_GCONF2,val)
        except:
           raise ErrorWritingRegister
           
    def getGestureGain(self):
        """
            Gets the gain of the photodiode during gesture mode
              Value    Gain
                0       1x
                1       2x
                2       4x
                3       8x
            return the current photodiode gain. 0xFF on error.
        """
        
        try:
            val = self.write_read(self.REG_GCONF2, 1)
        except:
            raise ErrorReadingRegister
        
        #Shift and mask out GGAIN bits */
        val = (val >> 5) & 0b00000011;
    
        return val
    
    def setGestureGain(self, gain):

        """
            Sets the gain of the photodiode during gesture mode
         
                Value    Gain
                  0       1x
                  1       2x
                  2       4x
                  3       8x
         
            gain the value for the photodiode gain
            return True if operation successful. False otherwise.
        """
        try:
            val = self.write_read(self.REG_GCONF2, 1)
        except:
            raise ErrorReadingRegister
            
        # Set bits in register to given value
        gain &= 0b00000011
        gain = gain << 5
        val &= 0b10011111
        val |= gain
        
        #Write register value back into GCONF2 register
        try:       
            self.write_bytes(self.REG_GCONF2,val)
            
        except:
           raise ErrorWritingRegister
     
    
    def get_device_id(self):
        n = self.write_read(REG_ID, 1)
        return hex(n[0])
    
   
    def getMode(self):
        """ 
            Reads and returns the contents of the ENABLE register
            Contents of the ENABLE register. 0xFF if error.
        """
        try:
            enable_value = self.write_read(REG_ENABLE, 1)
        except:
            return ERROR;
        
        return enable_value;

    def setMode(self, mode, enable):

        reg_val = self.getMode()

        if reg_val == ERROR :
            return False
        
        enable = enable & 0x01
        if mode >= 0 and mode <= 6:
            if enable== ENABLE_ON:
                reg_val |= (1 << mode)
            else:
                reg_val &= ~(1 << mode)
        elif mode == ENABLE_ALL :
            if enable == ENABLE_ON:
                reg_val = 0x7F;
            else:
                reg_val = 0x00
        
        try:       
            self.write_bytes(REG_ENABLE,reg_val)
            return True
        except:
            return False
     
    def getLEDBoost(self):
        """    
            brief Get the current LED boost value
            Value  Boost Current
              0        100%
              1        150%
              2        200%
              3        300%
         
             The LED boost value. 0xFF on failure.
        """
        
        #Read value from CONFIG2 register
        try:
            val = self.write_read(REG_CONFIG2, 1)
        except:
            return ERROR
            
        val = (val >> 4) & 0b00000011 #Shift and mask out LED_BOOST bits
        return val

    def setLEDBoost(self, boost):
        #Read value from CONFIG2 register 
        val = self.write_read(REG_CONFIG2, 1)

        # Set bits in register to given value
        boost &= 0b00000011
        boost = boost << 4
        val &= 0b11001111
        val |= boost
    
        # Write register value back into CONFIG2 register
        try:       
            self.write_bytes(REG_CONFIG2, val)
            return True
        except:
            return False
     
    def enableGestureSensor(self, interrupts):
        """ 
        Starts the gesture recognition engine on the APDS-9960
        
        Enable gesture mode
        Set ENABLE to 0 (power off)
        Set WTIME to 0xFF
        Set AUX to LED_BOOST_300
        Enable PON, WEN, PEN, GEN in ENABLE
        """ 
        self.resetGestureParameters()
        
        self.write_bytes(REG_WTIME, 0xFF)
        self.write_bytes(REG_PPULSE, DEFAULT_GESTURE_PPULSE)

        self.setLEDBoost(LED_BOOST_300)
     
        # if( interrupts ) {
        #     if( !setGestureIntEnable(1) ) {
        #         return false;
        #     }
        # } else {
        #     if( !setGestureIntEnable(0) ) {
        #         return false;
        #     }
        # }
    
    
        if not self.setGestureMode(1):
            return False

        if not self.enablePower():
            return False

        if not self.setMode(ENABLE_WAIT, 1):
            return False

        if not self.setMode(ENABLE_PROXIMITY, 1):
            return False
    
        if not self.setMode(ENABLE_GESTURE, 1):
            return False
    
    
        return True

    def enablePower(self):
        """ 
        Turn the APDS-9960 on
        return True if operation successful. False otherwise.
        """
        if not self.setMode(ENABLE_POWER, 1):
            return False
        
        return True;

    def disablePower(self):
        """
            Turn the APDS-9960 off
            return True if operation successful. False otherwise.
        """

        if not self.setMode(ENABLE_POWER, 0):
            return False
        
        return True
 
    def setGestureMode(self, mode):
        
        """
            Tells the state machine to either enter or exit gesture state machine
            mode 1 to enter gesture state machine, 0 to exit.
            True if operation successful. False otherwise.
        """
        val = self.write_read(REG_GCONF4, 1)
    
        #Set bits in register to given value */
        mode &= 0b00000001;
        val &= 0b11111110;
        val |= mode;
    
        try:       
            self.write_bytes(REG_GCONF4, val)
            return True
        except:
            return False
   
    def isGestureAvailable(self):
        
        """ 
            Determines if there is a gesture available for reading
            return True if gesture available. False otherwise.
        """
        
        #Read value from GSTATUS register
        try:
            val = self.write_read(REG_GSTATUS, 1)
        except:
            return ERROR
    
  
        #Shift and mask out GVALID bit
        val &= APDS9960_GVALID
    
        # Return true/false based on GVALID bit */
        if val == 1:
            return True
        else:
            return True
    
    def readGesture(self):
     
        """ 
            Processes a gesture event and returns best guessed gesture
            return Number corresponding to gesture. -1 on error.
        """

        fifo_level = 0

    
        #Make sure that power and gesture is on and data is valid */
        mode= self.getMode() & 0b01000001
        if not self.isGestureAvailable() or mode != 0b01000001 :
            return direction.DIR_NONE
    
        #Keep looping as long as gesture data is valid
        while True:
            #Wait some time to collect next batch of FIFO data
            sleep(self.FIFO_PAUSE_TIME)
            #Get the contents of the STATUS register. Is data still valid?
            try:
                gstatus = self.write_read(self.REG_GSTATUS, 1)
            except:
                return ERROR
        
            #If we have valid data, read in FIFO
            if (gstatus & self.REG_GVALID) == self.REG_GVALID:
        
                #Read the current FIFO level
                try:
                    fifo_level = self.write_read(self.REG_GFLVL, 1)
                except:
                    return ERROR

                if DEBUG:
                    print("FIFO Level: ", fifo_level)
                

                #If there's stuff in the FIFO, read it into our data block */
                if fifo_level > 0:
                
                    fifo_data = self.write_read(self.REG_GFIFO_U,fifo_level * 4)
    
                    # If at least 1 set of data, sort the data into U/D/L/R */
                    for i  in range(0 ,len(fifo_data), 4) :
                        self.gesture_data_.u_data[self.gesture_data_.index] = fifo_data[i + 0]
                        self.gesture_data_.d_data[self.gesture_data_.index] = fifo_data[i + 1]
                        self.gesture_data_.l_data[self.gesture_data_.index] = fifo_data[i + 2]
                        self.gesture_data_.r_data[self.gesture_data_.index] = fifo_data[i + 3]
                        self.gesture_data_.index+=1
                        self.gesture_data_.total_gestures+=1
                    
                    
                    #Filter and process gesture data. Decode near/far state
                    if self.processGestureData():
                        if self.decodeGesture():
        
                            print(self.gesture_motion_)

                    self.self.gesture_data_.index = 0;
                    self.self.gesture_data_.total_gestures = 0;
          
                else:
    
                    #Determine best guessed gesture and clean up */
                    sleep(self.FIFO_PAUSE_TIME)
                    self.decodeGesture()
                    motion = self.gesture_motion_

                    print("END: ")
                    print(self.gesture_motion_)
                    self.resetGestureParameters()
                    return motion
                    
    def processGestureData(self):
        """
            Processes the raw gesture data to determine swipe direction
            return True if near or far state seen. False otherwise.
        """

        u_first = 0
        d_first = 0
        l_first = 0
        r_first = 0
        u_last = 0
        d_last = 0
        l_last = 0
        r_last = 0
     

        #If we have less than 4 total gestures, that's not enough 
        if self.gesture_data_.total_gestures <= 4:
            return False
    
    
        #Check to make sure our data isn't out of bounds
        if self.gesture_data_.total_gestures <= 32 and self.gesture_data_.total_gestures > 0:
        
            #Find the first value in U/D/L/R above the threshold
            for i in range(0, self.gesture_data_.total_gestures) :
                if (self.self.gesture_data_.u_data[i] >  self.GESTURE_THRESHOLD_OUT) and (self.self.gesture_data_.d_data[i] > self.GESTURE_THRESHOLD_OUT) and (self.self.gesture_data_.l_data[i] > self.GESTURE_THRESHOLD_OUT) and (self.self.gesture_data_.r_data[i] > self.GESTURE_THRESHOLD_OUT):
                    
                    u_first = self.self.gesture_data_.u_data[i]
                    d_first = self.self.gesture_data_.d_data[i]
                    l_first = self.self.gesture_data_.l_data[i]
                    r_first = self.self.gesture_data_.r_data[i]
                    break
                
            
        
        #If one of the _first values is 0, then there is no good data 
        if (u_first == 0) or (d_first == 0) or (l_first == 0) or (r_first == 0) :
            return False
        
        # Find the last value in U/D/L/R above the threshold
        #for i = self.gesture_data_.total_gestures - 1; i >= 0; i-- : 
        for i in reversed(range(self.self.gesture_data_.total_gestures)):
            if DEBUG:
                print("Finding last: ")
                print("U:" , self.gesture_data_.u_data[i])
                print(" D:", self.gesture_data_.d_data[i])
                print(" L:", self.gesture_data_.l_data[i])
                print(" R:", self.gesture_data_.r_data[i])
                
            if (self.gesture_data_.u_data[i] > self.GESTURE_THRESHOLD_OUT) and (self.gesture_data_.d_data[i] > self.GESTURE_THRESHOLD_OUT) and (self.gesture_data_.l_data[i] > self.GESTURE_THRESHOLD_OUT) and (self.gesture_data_.r_data[i] > self.GESTURE_THRESHOLD_OUT) :
                
                    u_last = self.gesture_data_.u_data[i]
                    d_last = self.gesture_data_.d_data[i]
                    l_last = self.gesture_data_.l_data[i]
                    r_last = self.gesture_data_.r_data[i]
                    break
            
        
    
    
        #Calculate the first vs. last ratio of up/down and left/right */
        ud_ratio_first = ((u_first - d_first) * 100) / (u_first + d_first);
        lr_ratio_first = ((l_first - r_first) * 100) / (l_first + r_first);
        ud_ratio_last = ((u_last - d_last) * 100) / (u_last + d_last);
        lr_ratio_last = ((l_last - r_last) * 100) / (l_last + r_last);
       
        if DEBUG:
            print("Last Values: ")
            print("U: ", u_last)
            print(" D: ",d_last)
            print(" L: ", l_last)
            print(" R: ", r_last)

            print("Ratios: ")
            print("UD Fi: " , ud_ratio_first)
            print(" UD La: " , ud_ratio_last)
            print(" LR Fi: ", lr_ratio_first)
            print(" LR La: ", lr_ratio_last)

       
        # Determine the difference between the first and last ratios */
        ud_delta = ud_ratio_last - ud_ratio_first;
        lr_delta = lr_ratio_last - lr_ratio_first;
    
        if DEBUG:
            print("Deltas: ")
            print("UD: " ,ud_delta)
            print(" LR: " , lr_delta)

        #Accumulate the UD and LR delta values */
        self.gesture_ud_delta_ += ud_delta;
        self.gesture_lr_delta_ += lr_delta;
        
        if DEBUG:
            print("Accumulations: ");
            print("UD: " , self.gesture_ud_delta_)
            print(" LR: ", self.gesture_lr_delta_)

    
        #Determine U/D gesture */
        if self.gesture_ud_delta_ >= self.GESTURE_SENSITIVITY_1 :
            self.gesture_ud_count_ = 1
        elif self.gesture_ud_delta_ <= -self.GESTURE_SENSITIVITY_1 :
            self.gesture_ud_count_ = -1
        else:
            self.gesture_ud_count_ = 0
    
    
        # Determine L/R gesture */
        if self.gesture_lr_delta_ >= self.GESTURE_SENSITIVITY_1:
            self.gesture_lr_count_ = 1
        elif self.gesture_lr_delta_ <= -self.GESTURE_SENSITIVITY_1:
            self.gesture_lr_count_ = -1
        else: 
            self.gesture_lr_count_ = 0
    
    
        #Determine Near/Far gesture */
        if self.gesture_ud_count_ == 0 and self.gesture_lr_count_ == 0:
            if abs(ud_delta) < self.GESTURE_SENSITIVITY_2 and  abs(lr_delta) < self.GESTURE_SENSITIVITY_2:
            
                if ud_delta == 0 and lr_delta == 0:
                    self.gesture_near_count_+=1
                elif ud_delta != 0 or lr_delta != 0:
                    self.gesture_far_count_+=1
            
            
                if  self.gesture_near_count_ >= 10 and self.gesture_far_count_ >= 2:
                    if ud_delta == 0 and lr_delta == 0:
                        self.gesture_state_ = direction.NEAR_STATE
                    elif ud_delta != 0 and lr_delta != 0:
                        self.gesture_state_ = direction.FAR_STATE
                    
                    return True
        
        else:
            if abs(ud_delta) < self.GESTURE_SENSITIVITY_2 and abs(lr_delta) < self.GESTURE_SENSITIVITY_2:
                
                if (ud_delta == 0) and (lr_delta == 0):
                    self.gesture_near_count_+=1
            
            
                if self.gesture_near_count_ >= 10:
                    self.gesture_ud_count_ = 0
                    self.gesture_lr_count_ = 0
                    self.gesture_ud_delta_ = 0
                    self.gesture_lr_delta_ = 0
            
        
    
    
        if DEBUG:
            print("UD_CT: " , self.gesture_ud_count_)
            print(" LR_CT: ", self.gesture_lr_count_)
            print(" NEAR_CT: ", self.gesture_near_count_)
            print(" FAR_CT: ", self.gesture_far_count_)
            print("----------")

        return False

    def decodeGesture(self):
        
        """ 
            Determines swipe direction or near/far state
            return True if near/far event. False otherwise.
        """

        #Return if near or far event is detected */
        if self.gesture_state_ == direction.NEAR_STATE:
            self.gesture_motion_ = direction.DIR_NEAR
            return True
        elif self.gesture_state_ == direction.FAR_STATE:
            self.gesture_motion_ = direction.DIR_FAR
            return True
    
    
        #Determine swipe direction
        if self.gesture_ud_count_ == -1 and self.gesture_lr_count_ == 0:
            self.gesture_motion_ = direction.DIR_UP
        elif self.gesture_ud_count_ == 1 and self.gesture_lr_count_ == 0:
            self.gesture_motion_ = direction.DIR_DOWN
        elif (self.gesture_ud_count_ == 0) and (self.gesture_lr_count_ == 1):
            self.gesture_motion_ = direction.DIR_RIGHT
        elif (self.gesture_ud_count_ == 0) and (self.gesture_lr_count_ == -1):
            self.gesture_motion_ = direction.DIR_LEFT
        elif (self.gesture_ud_count_ == -1) and (self.gesture_lr_count_ == 1):
            if abs(self.gesture_ud_delta_) > abs(self.gesture_lr_delta_):
                self.gesture_motion_ = direction.DIR_UP
            else:
                self.gesture_motion_ = direction.DIR_RIGHT
        
        elif (self.gesture_ud_count_ == 1) and (self.gesture_lr_count_ == -1):
            if abs(self.gesture_ud_delta_) > abs(self.gesture_lr_delta_):
                self.gesture_motion_ = direction.DIR_DOWN
            else:
                self.gesture_motion_ = direction.DIR_LEFT
        
        elif(self.gesture_ud_count_ == -1) and (self.gesture_lr_count_ == -1):
            if abs(self.gesture_ud_delta_) > abs(self.gesture_lr_delta_):
                self.gesture_motion_ = direction.DIR_UP
            else:
                self.gesture_motion_ = direction.DIR_LEFT
            
        elif(self.gesture_ud_count_ == 1) and (self.gesture_lr_count_ == 1):
            if abs(self.gesture_ud_delta_) > abs(self.gesture_lr_delta_):
                self.gesture_motion_ = direction.DIR_DOWN
            else:
                self.gesture_motion_ = direction.DIR_RIGHT
            
        else:
            return False
        
    
        return True

 
