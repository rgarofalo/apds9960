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


new_exception(RuntimeErrorSet,ValueError,'Cannot override values')
new_exception(RuntimeErrorDel,ValueError,'Cannot delete values')
new_exception(ErrorReadingRegister,RuntimeError,'It was an error while reading the register')
new_exception(ErrorWritingRegister,RuntimeError,'There was an error writing to the register')
new_exception(ErrorDevice,RuntimeError,'Error device 0xFF')



#Debug 
DEBUG =     0

#APDS-9960 I2C address 
APDS9960_I2C_ADDR  =     0x39

#Gesture parameters 
GESTURE_THRESHOLD_OUT =  10
GESTURE_SENSITIVITY_1 =  50
GESTURE_SENSITIVITY_2 =  20

#Error code for returned values 
ERROR      =             0xFF

#Acceptable device IDs 
APDS9960_ID_1   =        0xAB
APDS9960_ID_2   =        0x9C 

#Misc parameters 
FIFO_PAUSE_TIME =        30      # Wait period (ms) between FIFO reads

#APDS-9960 register addresses 
APDS9960_ENABLE =        0x80
APDS9960_ATIME  =       0x81
APDS9960_WTIME  =        0x83
APDS9960_AILTL  =        0x84
APDS9960_AILTH  =        0x85
APDS9960_AIHTL  =        0x86
APDS9960_AIHTH  =        0x87
APDS9960_PILT   =        0x89
APDS9960_PIHT   =        0x8B
APDS9960_PERS    =      0x8C
APDS9960_CONFIG1 =      0x8D
APDS9960_PPULSE  =      0x8E
APDS9960_CONTROL =      0x8F
APDS9960_CONFIG2 =      0x90
APDS9960_ID      =      0x92
APDS9960_STATUS  =      0x93
APDS9960_CDATAL  =      0x94
APDS9960_CDATAH  =      0x95
APDS9960_RDATAL  =      0x96
APDS9960_RDATAH  =      0x97
APDS9960_GDATAL  =      0x98
APDS9960_GDATAH  =      0x99
APDS9960_BDATAL  =      0x9A
APDS9960_BDATAH  =      0x9B
APDS9960_PDATA   =      0x9C
APDS9960_POFFSET_UR =   0x9D
APDS9960_POFFSET_DL =   0x9E
APDS9960_CONFIG3    =   0x9F
APDS9960_GPENTH     =   0xA0
APDS9960_GEXTH      =   0xA1
APDS9960_GCONF1     =   0xA2
APDS9960_GCONF2     =   0xA3
APDS9960_GOFFSET_U  =   0xA4
APDS9960_GOFFSET_D  =   0xA5
APDS9960_GOFFSET_L  =   0xA7
APDS9960_GOFFSET_R  =   0xA9
APDS9960_GPULSE     =   0xA6
APDS9960_GCONF3     =   0xAA
APDS9960_GCONF4     =   0xAB
APDS9960_GFLVL      =   0xAE
APDS9960_GSTATUS    =   0xAF
APDS9960_IFORCE     =   0xE4
APDS9960_PICLEAR    =   0xE5
APDS9960_CICLEAR    =   0xE6
APDS9960_AICLEAR    =   0xE7
APDS9960_GFIFO_U    =   0xFC
APDS9960_GFIFO_D    =   0xFD
APDS9960_GFIFO_L    =   0xFE
APDS9960_GFIFO_R    =   0xFF

#Bit fields 
APDS9960_PON        =   0b00000001
APDS9960_AEN        =   0b00000010
APDS9960_PEN        =   0b00000100
APDS9960_WEN        =   0b00001000
APSD9960_AIEN       =   0b00010000
APDS9960_PIEN       =   0b00100000
APDS9960_GEN        =   0b01000000
APDS9960_GVALID     =   0b00000001

#On/Off definitions 
OFF                 =    0
ON                  =    1

#Acceptable parameters for self.setMode 
POWER                =   0
AMBIENT_LIGHT        =   1
PROXIMITY            =   2
WAIT                 =   3
AMBIENT_LIGHT_INT    =   4
PROXIMITY_INT        =   5
GESTURE              =   6
ALL                  =   7

#LED Drive values 
LED_DRIVE_100MA      =   0
LED_DRIVE_50MA       =   1
LED_DRIVE_25MA       =   2
LED_DRIVE_12_5MA     =   3

#Proximity Gain (PGAIN) values 
PGAIN_1X             =   0
PGAIN_2X             =   1
PGAIN_4X             =   2
PGAIN_8X             =   3

#ALS Gain (AGAIN) values 
AGAIN_1X             =  0
AGAIN_4X             =  1
AGAIN_16X            =  2
AGAIN_64X            =  3

#Gesture Gain (GGAIN) values 
GGAIN_1X             =  0
GGAIN_2X             =  1
GGAIN_4X             =  2
GGAIN_8X             =  3

#LED Boost values 
LED_BOOST_100        =  0
LED_BOOST_150        =  1
LED_BOOST_200        =  2
LED_BOOST_300        =  3    

#Gesture wait time values 
GWTIME_0MS           =  0
GWTIME_2_8MS         =  1
GWTIME_5_6MS         =  2
GWTIME_8_4MS         =  3
GWTIME_14_0MS        =  4
GWTIME_22_4MS        =   5
GWTIME_30_8MS        =   6
GWTIME_39_2MS        =   7

#Default values 
DEFAULT_ATIME        =   219     # 103ms
DEFAULT_WTIME        =   246     # 27ms
DEFAULT_PROX_PPULSE  =   0x87    # 16us, 8 pulses
DEFAULT_GESTURE_PPULSE = 0x89    # 16us, 10 pulses
DEFAULT_POFFSET_UR     = 0       # 0 offset
DEFAULT_POFFSET_DL    =  0       # 0 offset      
DEFAULT_CONFIG1       =  0x60    # No 12x wait (WTIME) factor
DEFAULT_LDRIVE        =  LED_DRIVE_100MA
DEFAULT_PGAIN         =   PGAIN_4X
DEFAULT_AGAIN         =  AGAIN_4X
DEFAULT_PILT          =  0       # Low proximity threshold
DEFAULT_PIHT          =  50      # High proximity threshold
DEFAULT_AILT          =  0xFFFF  # Force interrupt for calibration
DEFAULT_AIHT          =  0
DEFAULT_PERS          =  0x11    # 2 consecutive prox or ALS for int.
DEFAULT_CONFIG2       =  0x01    # No saturation interrupts or LED boost  
DEFAULT_CONFIG3       =  0       # Enable all photodiodes, no SAI
DEFAULT_GPENTH        =  40      # Threshold for entering gesture mode
DEFAULT_GEXTH         =  30      # Threshold for exiting gesture mode    
DEFAULT_GCONF1        =  0x40    # 4 gesture events for int., 1 for exit
DEFAULT_GGAIN         =  GGAIN_4X
DEFAULT_GLDRIVE       =  LED_DRIVE_100MA
DEFAULT_GWTIME        =  GWTIME_2_8MS
DEFAULT_GOFFSET       =  0       # No offset scaling for gesture mode
DEFAULT_GPULSE        =  0xC9    # 32us, 10 pulses
DEFAULT_GCONF3        =  0       # All photodiodes active during gesture
DEFAULT_GIEN          =  0       # Disable gesture interrupts

#Direction definitions 

DIR_NONE = 'DIR_NONE'
DIR_LEFT = 'DIR_LEFT'
DIR_RIGHT ='DIR_RIGHT'
DIR_UP = 'DIR_UP'
DIR_DOWN = 'DIR_DOWN'
DIR_NEAR = 'DIR_NEAR'
DIR_FAR= 'DIR_FAR'
DIR_ALL= 'DIR_ALL'



#State definitions 

NA_STATE = 'NA_STATE'
NEAR_STATE = 'NEAR_STATE'
FAR_STATE = 'FAR_STATE'
ALL_STATE = 'ALL_STATE'


class gesture_data_type():
    def __init__(self):
        self.u_data=[0 for x in range(32)]
        self.d_data=[0 for x in range(32)] 
        self.l_data=[0 for x in range(32)]
        self.r_data=[0 for x in range(32)]
        self.index = 0
        self.total_gestures = 0
        self.in_threshold = 0
        self.out_threshold = 0

class APDS9960(i2c.I2C):
    """
    ==================
    The APDS9960 class
    ==================

.. class:: APDS9960(drivername)
     """
     
     
    def __init__(self, i2cdrv, addr=0x39, clk=100000):
        try:
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
            self.gesture_motion_ = DIR_NONE
            self.gesture_data_= gesture_data_type()
        except Exception as e:
            print(e)

    def printRegister(self):

        try:
            self._printDEBUG('APDS9960_ENABLE',self.write_read(APDS9960_ENABLE, 1)[0])
            self._printDEBUG('APDS9960_CONFIG1',self.write_read(APDS9960_CONFIG1, 1)[0])

            self._printDEBUG('APDS9960_CONTROL',self.write_read(APDS9960_CONTROL, 1)[0])
            self._printDEBUG('APDS9960_CONFIG2',self.write_read(APDS9960_CONFIG2, 1)[0])
            self._printDEBUG('APDS9960_STATUS',self.write_read(APDS9960_STATUS, 1)[0])
            self._printDEBUG('APDS9960_CONFIG3',self.write_read(APDS9960_CONFIG3, 1)[0])
            self._printDEBUG('APDS9960_GCONF3',self.write_read(APDS9960_GCONF3, 1)[0])
            self._printDEBUG('APDS9960_GCONF4',self.write_read(APDS9960_GCONF4, 1)[0])
            self._printDEBUG('APDS9960_GCONF2',self.write_read(APDS9960_GCONF2, 1)[0])
          
        except:
            raise ErrorReadingRegister
        



    def initialize(self):

        try:

       
            # Read ID register and check against known values for APDS-9960 */
            if (self.get_device_id()!= 0xAB):
                return False

            # Set ENABLE register to 0 (disable all features) */
            self.setMode(ALL, OFF)

            # Set default values for ambient light and proximity registers */
            self._write_bytes(APDS9960_ATIME, DEFAULT_ATIME)
            self._write_bytes(APDS9960_WTIME, DEFAULT_WTIME)
            self._write_bytes(APDS9960_PPULSE, DEFAULT_PROX_PPULSE)
            self._write_bytes(APDS9960_POFFSET_UR, DEFAULT_POFFSET_UR)#
            self._write_bytes(APDS9960_POFFSET_DL, DEFAULT_POFFSET_DL)#
            self._write_bytes(APDS9960_CONFIG1, DEFAULT_CONFIG1)#
        
            self.setLEDDrive(DEFAULT_LDRIVE)#APDS9960_CONTROL
            
            self.setProximityGain(DEFAULT_PGAIN)#APDS9960_CONTROL
            
            self.setAmbientLightGain(DEFAULT_AGAIN)
            
            self.setProxIntLowThresh(DEFAULT_PILT)
            
            self.setProxIntHighThresh(DEFAULT_PIHT)
            
            self.setLightIntLowThreshold(DEFAULT_AILT)
            
            self.setLightIntHighThreshold(DEFAULT_AIHT)
            
            self._write_bytes(APDS9960_PERS, DEFAULT_PERS)
            
            self._write_bytes(APDS9960_CONFIG2, DEFAULT_CONFIG2)
            
            self._write_bytes(APDS9960_CONFIG3, DEFAULT_CONFIG3)
            
            # Set default values for gesture sense registers */
            self.setGestureEnterThresh(DEFAULT_GPENTH)
            
            self.setGestureExitThresh(DEFAULT_GEXTH)
            
            self._write_bytes(APDS9960_GCONF1, DEFAULT_GCONF1)
            
            self.setGestureGain(DEFAULT_GGAIN)
            
            self.setGestureLEDDrive(DEFAULT_GLDRIVE)
            
            self.setGestureWaitTime(DEFAULT_GWTIME)
            
            self._write_bytes(APDS9960_GOFFSET_U, DEFAULT_GOFFSET)
            
            self._write_bytes(APDS9960_GOFFSET_D, DEFAULT_GOFFSET)
            
            self._write_bytes(APDS9960_GOFFSET_L, DEFAULT_GOFFSET)
            
            self._write_bytes(APDS9960_GOFFSET_R, DEFAULT_GOFFSET)
            
            self._write_bytes(APDS9960_GPULSE, DEFAULT_GPULSE)
            
            self._write_bytes(APDS9960_GCONF3, DEFAULT_GCONF3)
            
            self.setGestureIntEnable(DEFAULT_GIEN)

        except Exception as e:
            print(e)
        
    def get_device_id(self):
        n = self.write_read(APDS9960_ID, 1)
        return n[0]

    def getMode(self):
        """ 
            .. method:: getMode()
            
                Reads and returns the contents of the ENABLE register
        """
        
        try:
            enable_value = self.write_read(APDS9960_ENABLE, 1)[0]
        except:
            raise ErrorReadingRegister
        
        return enable_value

    
    def setMode(self, mode, enable):
        """ 
            .. method:: setMode(mode, enable)
            
                Enables or disables a feature in the APDS-9960
                mode: feature to enable
                enable: ON (1) or OFF (0)
        """

        reg_val = self.getMode()

        if reg_val == ERROR :
            raise ErrorDevice
        
        # Change bit(s) in ENABLE register */
        enable = enable & 0x01
        if mode >= 0 and mode <= 6 :
            if (enable):
                reg_val |= (1 << mode)
            else: 
                reg_val &= ~(1 << mode)
            
        elif mode == ALL:
            if (enable): 
                reg_val = 0x7F
            else: 
                reg_val = 0x00
        
        self._write_bytes(APDS9960_ENABLE,reg_val)
       

    def enableLightSensor(self, interrupts):
        """
            .. method:: enableLightSensor(interrupts)
            
                Starts the light (R/G/B/Ambient) sensor on the APDS-9960
                interrupts True to enable hardware interrupt on high or low light
        """

        # Set default gain, interrupts, enable power, and enable sensor */
        self.setAmbientLightGain(DEFAULT_AGAIN) 
        
        if interrupts:
            self.setAmbientLightIntEnable(1)
        else: 
            self.setAmbientLightIntEnable(0)
                    
        self.enablePower()
        self.setMode(AMBIENT_LIGHT, 1)

    def disableLightSensor(self):
        """
            .. method:: disableLightSensor()

                Ends the light sensor on the APDS-9960
        """

        self.setAmbientLightIntEnable(0)
        self.setMode(AMBIENT_LIGHT, 0)

    def enableProximitySensor(self, interrupts):
        """ 
            .. method:: enableProximitySensor(interrupts)

                Starts the proximity sensor on the APDS-9960
                interrupts True to enable hardware external interrupt on proximity
        """

        # Set default gain, LED, interrupts, enable power, and enable sensor */
        self.setProximityGain(DEFAULT_PGAIN)
        self.setLEDDrive(DEFAULT_LDRIVE)
       
        if interrupts:
            self.setProximityIntEnable(1)
        else: 
            self.setProximityIntEnable(0)
            
        self.enablePower()
        self.setMode(PROXIMITY, 1)

    def disableProximitySensor(self):
        """
            .. method:: disableProximitySensor()
            
                Ends the proximity sensor on the APDS-9960
        """

        self.setProximityIntEnable(0)
        self.setMode(PROXIMITY, 0)    


    def enableGestureSensor(self, interrupts):
        """
            .. method:: enableGestureSensor(interrupts)

                Starts the gesture recognition engine on the APDS-9960
                
                Enable gesture mode
                Set ENABLE to 0 (power off)
                Set WTIME to 0xFF
                Set AUX to LED_BOOST_300
                Enable PON, WEN, PEN, GEN in ENABLE
                
        """ 
        self.resetGestureParameters()
        self._write_bytes(APDS9960_WTIME, 0xFF)
        
        self._write_bytes(APDS9960_PPULSE, DEFAULT_GESTURE_PPULSE)
    
        self.setLEDBoost(LED_BOOST_300)

        if interrupts:
            self.setGestureIntEnable(1)
        else:
            self.setGestureIntEnable(0)
    
        self.setGestureMode(1)
        self.enablePower(self)
        self.setMode(WAIT, 1)
        self.setMode(PROXIMITY, 1)
        self.setMode(GESTURE, 1)



    def disableGestureSensor(self):
        """
            .. method:: disableGestureSensor()
            
                Ends the gesture recognition engine on the APDS-9960
        """

        self.resetGestureParameters()
        self.setGestureIntEnable(0) 
        self.setGestureMode(0)
        self.setMode(GESTURE, 0)
        
        
    def isGestureAvailable(self):
        """ 
            .. method:: isGestureAvailable()
                
                Determines if there is a gesture available for reading
                return True if gesture available. False otherwise.
        """

        #Read value from GSTATUS register
        try:
            val = self.write_read(APDS9960_GSTATUS, 1)[0]
        except:
             raise ErrorReadingRegister
    
        # Shift and mask out GVALID bit */
        val &= APDS9960_GVALID
        
        # Return True/False based on GVALID bit */
        if val == 1:
            return True
        else:
            return False
    


    def readGesture(self):
        """ 
            .. method:: readGesture()
            
                Processes a gesture event and returns best guessed gesture
                return Number corresponding to gesture.
        """

        fifo_level = 0
        fifo_data =[]
        
        # Make sure that power and gesture is on and data is valid */
        mode= self.getMode() & 0b01000001
        if not self.isGestureAvailable() or not mode:
            self._printDEBUG(' Make sure that power and gesture is on and data is valid')
            return DIR_NONE
        
        
        # Keep looping as long as gesture data is valid */
        while True:
        
            # Wait some time to collect next batch of FIFO data */
            sleep(FIFO_PAUSE_TIME)
            
            # Get the contents of the STATUS register. Is data still valid? */
            try:
                gstatus = self.write_read(APDS9960_GSTATUS, 1)[0]
            except:
                raise ErrorReadingRegister
            
            
            # If we have valid data, read in FIFO */
            if (gstatus & APDS9960_GVALID) == APDS9960_GVALID:
                 #Read the current FIFO level
                try:
                    fifo_level = self.write_read(APDS9960_GFLVL, 1)[0]
                except:
                    raise ErrorReadingRegister
            

                # If there's stuff in the FIFO, read it into our data block 
                self._printDEBUG("FIFO Level: ", fifo_level)

                if fifo_level > 0:

                    try:
                        fifo_data = self.write_read(APDS9960_GFIFO_U, fifo_level * 4)
                    except:
                        raise ErrorReadingRegister
                    
                    #self._printDEBUG("FIFO data: ", len(fifo_data))
                    #self._printDEBUG("FIFO Dump: ",fifo_data)
                    #sleep(1000)
                    # If at least 1 set of data, sort the data into U/D/L/R */
                    if len(fifo_data)>=4:
                        for i  in range(0 ,len(fifo_data), 4):
                            self.gesture_data_.u_data[self.gesture_data_.index]=fifo_data[i + 0]
                            self.gesture_data_.d_data[self.gesture_data_.index]=fifo_data[i + 1]
                            self.gesture_data_.l_data[self.gesture_data_.index]=fifo_data[i + 2]
                            self.gesture_data_.r_data[self.gesture_data_.index]=fifo_data[i + 3]
                            self.gesture_data_.index+=1
                            self.gesture_data_.total_gestures+=1
                            
                            self._printDEBUG("Finding First:","U:",fifo_data[i + 0],"D:",fifo_data[i + 1],"L:",fifo_data[i + 2],"R:",fifo_data[i + 3])

                        #self._printDEBUG("total_gestures: ",  self.gesture_data_.total_gestures)
                        
                        # # Filter and process gesture data. Decode near/far state */
                        if self._processGestureData():
                            if self._decodeGesture():
                                self._printDEBUG()

                        # Reset data */
                        self.gesture_data_.index = 0
                        self.gesture_data_.total_gestures = 0
                        # self.gesture_data_.u_data=[]
                        # self.gesture_data_.d_data=[]
                        # self.gesture_data_.l_data=[]
                        # self.gesture_data_.r_data=[]
                    
                
            else: 
               
                #Determine best guessed gesture and clean up */
                sleep(FIFO_PAUSE_TIME)
                if not self._decodeGesture():
                    self._printDEBUG('return decode False')

                motion = self.gesture_motion_
    
    
                self._printDEBUG("END: ")
                self._printDEBUG(self.gesture_motion_)
                self._printDEBUG(gstatus)
    
                self.resetGestureParameters()
                return motion

    def enablePower(self):
        """ 
            .. method::enablePower()
            
                Turn the APDS-9960 on
                
        """

        self.setMode(POWER, 1)
        
        
    def disablePower(self):
        """
            .. method::disablePower()
                
                Turn the APDS-9960 off
        """

        self.setMode(POWER, 0)
        


# #******************************************************************************
#  * Ambient light and color sensor controls
#  ******************************************************************************/

    def readAmbientLight(self):
        """
            .. method:: readAmbientLight()
            
                Reads the ambient (clear) light level as a 16-bit value
                return value of the light sensor.
        """
        try:
            valLow = self.write_read(APDS9960_CDATAL, 1)[0]
            valHight = self.write_read(APDS9960_CDATAH, 1)[0]
        except:
            raise ErrorReadingRegister
                    
        
        return valLow + (valHight << 8)
        


    def readRedLight(self):
        """
            .. method:: readRedLight()
                
                Reads the red light level as a 16-bit value
                return value of the light sensor.
        """
        
      
        try:
            valLow = self.write_read(APDS9960_RDATAL, 1)[0]
            valHight = self.write_read(APDS9960_RDATAH, 1)[0]
        except:
            raise ErrorReadingRegister
                    
        
        return valLow + (valHight << 8)

    def readGreenLight(self):
        """
            .. method:: readGreenLight()
                
                Reads the red light level as a 16-bit value
                return value of the light sensor.
        """
        
      
        try:
        
            valLow = self.write_read(APDS9960_GDATAL, 1)[0]
            valHight = self.write_read(APDS9960_GDATAH, 1)[0]
        except:
            raise ErrorReadingRegister
                    
        
        return valLow + (valHight << 8)
        
    
    def readBlueLight(self):
        """
            .. method:: readBlueLight()
                
                Reads the red light level as a 16-bit value
                return value of the light sensor.
        """
        
        try:
            valLow = self.write_read(APDS9960_BDATAL, 1)[0]
            valHight = self.write_read(APDS9960_BDATAH, 1)[0]
        except:
            raise ErrorReadingRegister
                    
        
        return valLow + (valHight << 8)
        
    


#  ******************************************************************************
#  * Proximity sensor controls
#  ******************************************************************************/


    def readProximity(self):
        """
            .. method:: readProximity()
            
                Reads the proximity level as an 8-bit value
                Return value of the proximity sensor.
        """
        
        try:
            val = self.write_read(APDS9960_PDATA, 1)[0]
        except:
            raise ErrorReadingRegister
                    
        
        return val
   
    
    def _processGestureData(self):

        u_first = 0
        d_first = 0
        l_first = 0
        r_first = 0
        u_last = 0
        d_last = 0
        l_last = 0
        r_last = 0
  
        # If we have less than 4 total gestures, that's not enough */
        if self.gesture_data_.total_gestures <= 4:
            self._printDEBUG('Tot_Gest:',self.gesture_data_.total_gestures)
            return False
        
        
        # Check to make sure our data isn't out of bounds */
        if self.gesture_data_.total_gestures <= 32 and self.gesture_data_.total_gestures > 0:
            
            # Find the first value in U/D/L/R above the threshold */
            for i in range(0, self.gesture_data_.total_gestures):

                if (self.gesture_data_.u_data[i] >  GESTURE_THRESHOLD_OUT) and (self.gesture_data_.d_data[i] > GESTURE_THRESHOLD_OUT) and (self.gesture_data_.l_data[i] > GESTURE_THRESHOLD_OUT) and (self.gesture_data_.r_data[i] > GESTURE_THRESHOLD_OUT):
                    u_first = self.gesture_data_.u_data[i]
                    d_first = self.gesture_data_.d_data[i]
                    l_first = self.gesture_data_.l_data[i]
                    r_first = self.gesture_data_.r_data[i]
                    break
                
            self._printDEBUG("Fist Values:","U:",u_first,"D:",d_first,"L:",l_first,"R:",r_first)

            
            # If one of the _first values is 0, then there is no good data */
            if (u_first == 0) or (d_first == 0) or (l_first == 0) or (r_first == 0):
                return False
            
            # Find the last value in U/D/L/R above the threshold */
            #for( i = gesture_data_.total_gestures - 1 i >= 0 i-- )
            l=range(self.gesture_data_.total_gestures)
            l=l[::-1]
            for i in l:
                

                if (self.gesture_data_.u_data[i] > GESTURE_THRESHOLD_OUT) and (self.gesture_data_.d_data[i] > GESTURE_THRESHOLD_OUT) and (self.gesture_data_.l_data[i] > GESTURE_THRESHOLD_OUT) and (self.gesture_data_.r_data[i] > GESTURE_THRESHOLD_OUT) :
                    
                    u_last = self.gesture_data_.u_data[i]
                    d_last = self.gesture_data_.d_data[i]
                    l_last = self.gesture_data_.l_data[i]
                    r_last = self.gesture_data_.r_data[i]

                    break
                
            
        
        
        # Calculate the first vs. last ratio of up/down and left/right */
        ud_ratio_first = ((u_first - d_first) * 100) / (u_first + d_first)
        lr_ratio_first = ((l_first - r_first) * 100) / (l_first + r_first)
        ud_ratio_last = ((u_last - d_last) * 100) / (u_last + d_last)
        lr_ratio_last = ((l_last - r_last) * 100) / (l_last + r_last)
           
        self._printDEBUG("Last Values:","U:", u_last,"D:",d_last,"L:", l_last,"R:", r_last)
        self._printDEBUG("Ratios:","UD First:",ud_ratio_first,"UD Last:" , ud_ratio_last,"LR Fi:", lr_ratio_first,"LR La:", lr_ratio_last)

       
        # Determine the difference between the first and last ratios */
        ud_delta = ud_ratio_last - ud_ratio_first;
        lr_delta = lr_ratio_last - lr_ratio_first;

        self._printDEBUG("Deltas:","UD: " ,ud_delta,"LR: " , lr_delta)

        #Accumulate the UD and LR delta values */
        self.gesture_ud_delta_ += ud_delta;
        self.gesture_lr_delta_ += lr_delta;
        
        self._printDEBUG("Accumulations:","UD:" , self.gesture_ud_delta_,"LR:", self.gesture_lr_delta_)

        
        # Determine U/D gesture */
        if self.gesture_ud_delta_ >= GESTURE_SENSITIVITY_1:
            self.gesture_ud_count_ = 1
        elif self.gesture_ud_delta_ <= -GESTURE_SENSITIVITY_1:
            self.gesture_ud_count_ = -1
        else:
            self.gesture_ud_count_ = 0
        
        
        # Determine L/R gesture */
        if self.gesture_lr_delta_ >= GESTURE_SENSITIVITY_1:
            self.gesture_lr_count_ = 1
        elif self.gesture_lr_delta_ <= -GESTURE_SENSITIVITY_1:
            self.gesture_lr_count_ = -1
        else: 
            self.gesture_lr_count_ = 0
        
        
        # Determine Near/Far gesture */
        if (self.gesture_ud_count_ == 0) and (self.gesture_lr_count_ == 0): 
            if (abs(ud_delta) < GESTURE_SENSITIVITY_2) and (abs(lr_delta) < GESTURE_SENSITIVITY_2): 
                
                if (ud_delta == 0) and (lr_delta == 0): 
                    self.gesture_near_count_+=1
                elif ud_delta != 0 or lr_delta != 0: 
                    self.gesture_far_count_+=1
                
                
                if (self.gesture_near_count_ >= 10) and (self.gesture_far_count_ >= 2): 
                    if (ud_delta == 0) and (lr_delta == 0): 
                        self.gesture_state_ = NEAR_STATE
                    elif ud_delta != 0 and lr_delta != 0: 
                        self.gesture_state_ = FAR_STATE
                    
                    return True
                
            
        else: 
            if (abs(ud_delta) < GESTURE_SENSITIVITY_2) and (abs(lr_delta) < GESTURE_SENSITIVITY_2): 
                    
                if (ud_delta == 0) and (lr_delta == 0): 
                    self.gesture_near_count_+=1
                
                
                if self.gesture_near_count_ >= 10:
                    self.gesture_ud_count_ = 0
                    self.gesture_lr_count_ = 0
                    self.gesture_ud_delta_ = 0
                    self.gesture_lr_delta_ = 0
                
            
        #self._printDEBUG("UD_CT: " , self.gesture_ud_count_,"LR_CT:", self.gesture_lr_count_,"NEAR_CT:", self.gesture_near_count_,"FAR_CT:", self.gesture_far_count_)
        self._printDEBUG("----------")

        return False


    def _decodeGesture(self):


        # Determines swipe direction or near/far state
        #return True if near/far event. False otherwise.
    
        self._printDEBUG('gesture_ud_delta_',self.gesture_ud_delta_)
        self._printDEBUG('gesture_lr_delta_',self.gesture_lr_delta_)
        self._printDEBUG('gesture_ud_count_',self.gesture_ud_count_)
        self._printDEBUG('gesture_lr_count_',self.gesture_lr_count_)
        
        self._printDEBUG('gesture_near_count_',self.gesture_near_count_)
        self._printDEBUG('gesture_far_count_',self.gesture_far_count_)

        self._printDEBUG('gesture_state_',self.gesture_state_)

         
       
    
        try:
        # Return if near or far event is detected */
            if self.gesture_state_ == NEAR_STATE:
                self.gesture_motion_ = DIR_NEAR
                return True
            elif self.gesture_state_ == FAR_STATE:
                self.gesture_motion_ = DIR_FAR
                return True
        
        
            # Determine swipe direction */
            if (self.gesture_ud_count_ == -1) and (self.gesture_lr_count_ == 0): 
                self.gesture_motion_ = DIR_UP
            elif (self.gesture_ud_count_ == 1) and (self.gesture_lr_count_ == 0): 
                self.gesture_motion_ = DIR_DOWN
            elif (self.gesture_ud_count_ == 0) and (self.gesture_lr_count_ == 1): 
                self.gesture_motion_ = DIR_RIGHT
            elif (self.gesture_ud_count_ == 0) and (self.gesture_lr_count_ == -1): 
                self.gesture_motion_ = DIR_LEFT
            elif (self.gesture_ud_count_ == -1) and (self.gesture_lr_count_ == 1): 
                if abs(self.gesture_ud_delta_) > abs(self.gesture_lr_delta_): 
                    self.gesture_motion_ = DIR_UP
                else:
                    self.gesture_motion_ = DIR_RIGHT
                
            elif (self.gesture_ud_count_ == 1) and (self.gesture_lr_count_ == -1): 
                if abs(self.gesture_ud_delta_) > abs(self.gesture_lr_delta_): 
                    self.gesture_motion_ = DIR_DOWN
                else:
                    self.gesture_motion_ = DIR_LEFT
                
            elif (self.gesture_ud_count_ == -1) and (self.gesture_lr_count_ == -1): 
                if abs(self.gesture_ud_delta_) > abs(self.gesture_lr_delta_): 
                    self.gesture_motion_ = DIR_UP
                else:
                    self.gesture_motion_ = DIR_LEFT
                
            elif (self.gesture_ud_count_ == 1) and (self.gesture_lr_count_ == 1): 
                if abs(self.gesture_ud_delta_) > abs(self.gesture_lr_delta_): 
                    self.gesture_motion_ = DIR_DOWN
                else:
                    self.gesture_motion_ = DIR_RIGHT
                
            else: 
                self.gesture_motion_ = DIR_NONE
                return False
        
        
            return True
        
        except Exception as e:
            print(e)
            return False

    def _resetGestureParameters(self):
        #Resets all the parameters in the gesture data member

        self.gesture_data_.index = 0
        self.gesture_data_.total_gestures = 0
    
        self.gesture_ud_delta_ = 0
        self.gesture_lr_delta_ = 0
    
        self.gesture_ud_count_ = 0
        self.gesture_lr_count_ = 0
    
        self.gesture_near_count_ = 0
        self.gesture_far_count_ = 0
    
        self.gesture_state_ = 0
        self.gesture_motion_ = DIR_NONE


# #******************************************************************************
#  * Getters and setters for register values
#  ******************************************************************************/

    def getProxIntLowThresh(self):
        """
            .. method:: getProxIntLowThresh()
            
                Returns the lower threshold for proximity detection
            
        """
        
        try:
            val = self.write_read(APDS9960_PILT, 1)[0]
        except:
            raise ErrorReadingRegister
                    
        
        return val
  
    def setProxIntLowThresh(self, threshold):
        """
            .. method:: getProxIntLowThresh(threshold)
                
                Sets the lower threshold for proximity detection
        """
        
        
        self._write_bytes(APDS9960_PILT, threshold)
        
 


    def getProxIntHighThresh(self):
        """
            .. method:: getProxIntHighThresh()
            
                Returns the high threshold for proximity detection
            
        """
        
        try:
            val = self.write_read(APDS9960_PIHT, 1)[0]
        except:
            raise ErrorReadingRegister
                    
        return val


    def setProxIntHighThresh(self, threshold):
        """
            .. method:: setProxIntHighThresh(threshold)
            
                Sets the high threshold for proximity detection
            
        """

        self._write_bytes(APDS9960_PIHT, threshold)
            

    def getLEDDrive(self):
        """
            .. method:: getLEDDrive()
                
                Returns LED drive strength for proximity and ALS
                
                +------+-------------+
                |Value    LED Current
                  0        100 mA
                  1         50 mA
                  2         25 mA
                  3         12.5 mA
                
        """

        try:
            val = self.write_read(APDS9960_CONTROL, 1)[0]
        except:
            raise ErrorReadingRegister
                    

         # Shift and mask out LED drive bits */
        return (val >> 6) & 0b00000011

    def setLEDDrive(self, drive):
        """
            .. method:: setLEDDrive(drive)
            
                brief Sets the LED drive strength for proximity and ALS
                 
                    Value    LED Current
                      0        100 mA
                      1         50 mA
                      2         25 mA
                      3         12.5 mA
                 
                 drive the value (0-3) for the LED drive strength
                 
        """

        try:
            val = self.write_read(APDS9960_CONTROL, 1)[0]
        except:
            raise ErrorReadingRegister 

        
    
        # Set bits in register to given value */
        drive &= 0b00000011
        drive = drive << 6
        val &= 0b00111111
        val |= drive
        
        try:       
            self._write_bytes(APDS9960_CONTROL, val)
        except:
            raise ErrorWritingRegister
       



    def getProximityGain(self):

        """ 
            .. method:: getProximityGain()
            
                Returns receiver gain for proximity detection
                 
                +--------+---------+
                |  Value |  Gain   |
                +========+=========+
                |    0   |    1x   |
                +--------+---------+
                |    1   |    2x   |
                +--------+---------+
                |    2   |    4x   |
                +--------+---------+
                |    3   |    8x   |
                +--------+---------+
                 
                  return the value of the proximity gain.
        """
        try:
            val = self.write_read(APDS9960_CONTROL, 1)[0]
        except:
            raise ErrorReadingRegister
  
    
        # Shift and mask out PDRIVE bits */
        val = (val >> 2) & 0b00000011
        
        return val



    def setProximityGain(self, drive):
        """
            .. method:: setProximityGain(drive):
            
                Sets the receiver gain for proximity detection
                
                +--------+---------+
                |  Value |  Gain   |
                +========+=========+
                |    0   |    1x   |
                +--------+---------+
                |    1   |    2x   |
                +--------+---------+
                |    2   |    4x   |
                +--------+---------+
                |    3   |    8x   |
                +--------+---------+
                
                
                drive the value (0-3) for the gain
                return True if operation successful.
        """

        try:
            val = self.write_read(APDS9960_CONTROL, 1)[0]
        except:
            raise ErrorReadingRegister
  
    
        # Set bits in register to given value */
        drive &= 0b00000011
        drive = drive << 2
        val &= 0b11110011
        val |= drive
        
         #Write register value back into CONTROL register
        try:       
            self._write_bytes(APDS9960_CONTROL,val)
        except:
           raise ErrorWritingRegister
      
        
        return True


    def getAmbientLightGain(self):
        """
            .. method:: getAmbientLightGain()
            
                Returns receiver gain for the ambient light sensor (ALS)
            
                +--------+---------+
                |  Value |  Gain   |
                +========+=========+
                |    0   |    1x   |
                +--------+---------+
                |    1   |    4x   |
                +--------+---------+
                |    2   |    16x  |
                +--------+---------+
                |    3   |    64x  |
                +--------+---------+
                
            
                return the value of the ALS gain. 0xFF on failure.
        """
        try:
            val = self.write_read(APDS9960_CONTROL, 1)[0]
        except:
            raise ErrorReadingRegister
            
        #Shift and mask out ADRIVE bits */
        val &= 0b00000011
    
        return val

  
    def setAmbientLightGain(self, drive):
        """
            .. method:: setAmbientLightGain(drive)
            
                Sets the receiver gain for the ambient light sensor (ALS)
             
                +--------+---------+
                |  Value |  Gain   |
                +========+=========+
                |    0   |    1x   |
                +--------+---------+
                |    1   |    4x   |
                +--------+---------+
                |    2   |    16x  |
                +--------+---------+
                |    3   |    64x  |
                +--------+---------+
                
                 
                drive the value (0-3) for the gain
                return True if operation successful. False otherwise.
        """

        try:
            val = self.write_read(APDS9960_CONTROL, 1)[0]
        except:
            raise ErrorReadingRegister
        
        #Set bits in register to given value
        drive &= 0b00000011
        val &= 0b11111100
        val |= drive
    
         #Write register value back into CONTROL register
        try:       
            self._write_bytes(APDS9960_CONTROL,val)
        except:
           raise ErrorWritingRegister


    def getLEDBoost(self):
        """    
            .. method:: getLEDBoost()
            
                brief Get the current LED boost value
                
                +-------+----------------+
                | Value | Boost Current  |
                +=======+================+
                |  0    |  100%          |
                +-------+----------------+
                |  1    |  150%          |
                +-------+----------------+
                |  2    |  200%          |
                +-------+----------------+
                |  3    |  300%          |
                +-------+----------------+
                
                  
                  
                return the LED boost value.
        """
        
        #Read value from CONFIG2 register
        try:
            val = self.write_read(APDS9960_CONFIG2, 1)[0]
        except:
            raise ErrorReadingRegister 
            
        val = (val >> 4) & 0b00000011 #Shift and mask out LED_BOOST bits
        return val



    def setLEDBoost(self, boost):
        """
            .. method:: setLEDBoost(boost)
        """
        #Read value from CONFIG2 register
        try:
            val = self.write_read(APDS9960_CONFIG2, 1)[0]
        except:
            raise ErrorReadingRegister
            
        # Set bits in register to given value
        boost &= 0b00000011
        boost = boost << 4
        val &= 0b11001111
        val |= boost
    
        # Write register value back into CONFIG2 register
        try:       
            self._write_bytes(APDS9960_CONFIG2, val)
        except:
            raise ErrorWritingRegister


    def getProxGainCompEnable(self):
        """
            .. method:: getProxGainCompEnable()
                
                Gets proximity gain compensation enable
                return 1 if compensation is enabled. 0 if not. 
            
        """
        
        try:
            val = self.write_read(APDS9960_CONFIG3, 1)[0]
        except:
            raise ErrorReadingRegister 
            
         # Shift and mask out PCMP bits */
        val = (val >> 5) & 0b00000001
        
        return val


  
    def setProxGainCompEnable(self, enable):
        """
            .. method:: setProxGainCompEnable(enable)
                
                Sets the proximity gain compensation enable
                enable 1 to enable compensation. 0 to disable compensation.
            
        """
         
        try:
            val = self.write_read(APDS9960_CONFIG3, 1)[0]
        except:
            raise ErrorReadingRegister
            
        # Set bits in register to given value */
        enable &= 0b00000001
        enable = enable << 5
        val &= 0b11011111
        val |= enable
    
        # Write register value back into CONFIG2 register
        try:       
            self._write_bytes(APDS9960_CONFIG3, val)
        except:
            raise ErrorWritingRegister

   

    def getProxPhotoMask(self):
        """
            .. method:: getProxPhotoMask()
            
                Gets the current mask for enabled/disabled proximity photodiodes
                
                1 = disabled, 0 = enabled
                
                +-----+-----------------+
                | Bit |   Photodiode    |
                +=====+=================+
                | 3   |    UP           |
                +-----+-----------------+
                | 2   |    DOWN         |
                +-----+-----------------+
                | 1   |    LEFT         |
                +-----+-----------------+
                | 0   |    RIGHT        |
                +-----+-----------------+
            
        """
        
        try:
            val = self.write_read(APDS9960_CONFIG3, 1)[0]
        except:
            raise ErrorReadingRegister 
            
        
        # Mask out photodiode enable mask bits */
        val &= 0b00001111
        
        return val



    def setProxPhotoMask(self, mask):
        """
            .. method:: setProxPhotoMask(mask)
            
                Sets the mask for enabling/disabling proximity photodiodes
                
                1 = disabled, 0 = enabled
                
                +-----+-----------------+
                | Bit |   Photodiode    |
                +=====+=================+
                | 3   |    UP           |
                +-----+-----------------+
                | 2   |    DOWN         |
                +-----+-----------------+
                | 1   |    LEFT         |
                +-----+-----------------+
                | 0   |    RIGHT        |
                +-----+-----------------+

            
        """
        
        try:
            val = self.write_read(APDS9960_CONFIG3, 1)[0]
        except:
            raise ErrorReadingRegister 
            
        
        # Set bits in register to given value */
        mask &= 0b00001111
        val &= 0b11110000
        val |= mask
    
        try:       
            self._write_bytes(APDS9960_CONFIG3, val)
        except:
            raise ErrorWritingRegister


    def getGestureEnterThresh(self):
        """
            .. method:: getGestureEnterThresh()
                
                Gets the entry proximity threshold for gesture sensing
                Return Current entry proximity threshold.
                
                
        """
        
        
        try:
            val = self.write_read(APDS9960_GPENTH, 1)[0]
        except:
            raise ErrorReadingRegister 
        
        return val


    def setGestureEnterThresh(self, threshold):
        """
            .. method:: setGestureEnterThresh(threshold)
                
                Sets the entry proximity threshold for gesture sensing
                threshold: proximity value needed to start gesture mode
                
        """

        try:       
            self._write_bytes(APDS9960_GPENTH, threshold)
        except:
            raise ErrorWritingRegister



    def getGestureExitThresh(self):
        """
            .. method:: getGestureExitThresh()
                
                Gets the exit proximity threshold for gesture sensing
        """
        
        try:
            val = self.write_read(APDS9960_GEXTH, 1)[0]
        except:
            raise ErrorReadingRegister 
        
        return val


    def setGestureExitThresh(self, threshold):
        """
            .. method:: setGestureExitThresh(threshold)
                
                Sets the exit proximity threshold for gesture sensing
                threshold: proximity value needed to end gesture mode
                
                
        """
        
        
        try:       
            self._write_bytes(APDS9960_GEXTH, threshold)
        except:
            raise ErrorWritingRegister
      


    def getGestureGain(self):
        """
            .. method:: getGestureGain()
            
                Gets the gain of the photodiode during gesture mode
                
                   +--------+----------+
                    | Value  |  Gain    |
                    +========+==========+
                    |  0     |  1x      |
                    +--------+----------+
                    |  1     |  2x      |
                    +--------+----------+
                    |  2     |  4x      |
                    +--------+----------+
                    |  3     |  8x      |
                    +--------+----------+
                    
                return the current photodiode gain.
        """
        
        try:
            val = self.write_read(APDS9960_GCONF2, 1)
        except:
            raise ErrorReadingRegister
        
        #Shift and mask out GGAIN bits */
        val = (val >> 5) & 0b00000011;
    
        return val
    
    def setGestureGain(self, gain):
        """
            .. method:: setGestureGain(gain)
            
                Sets the gain of the photodiode during gesture mode
             
                    +--------+----------+
                    | Value  |  Gain    |
                    +========+==========+
                    |  0     |  1x      |
                    +--------+----------+
                    |  1     |  2x      |
                    +--------+----------+
                    |  2     |  4x      |
                    +--------+----------+
                    |  3     |  8x      |
                    +--------+----------+
            
                gain the value for the photodiode gain

        """
        try:
            val = self.write_read(APDS9960_GCONF2, 1)[0]
        except:
            raise ErrorReadingRegister
            
        # Set bits in register to given value
        gain &= 0b00000011
        gain = gain << 5
        val &= 0b10011111
        val |= gain
        
        #Write register value back into GCONF2 register
        try:       
            self._write_bytes(APDS9960_GCONF2,val)
            
        except:
           raise ErrorWritingRegister


    def getGestureLEDDrive(self):
        """
            .. method:: getGestureLEDDrive()
            
                Gets the drive current of the LED during gesture mode
             
                    +--------+--------------+
                    | Value  |  LED Current |
                    +========+==============+
                    |  0     |   100 mA     |
                    +--------+--------------+
                    |  1     |    50 mA     |
                    +--------+--------------+
                    |  2     |    25 mA     |
                    +--------+--------------+
                    |  3     |    12.5 mA   |
                    +--------+--------------+

             
               return the LED drive current value.
        """
        try:
            val = self.write_read(APDS9960_GCONF2, 1)[0]
        except:
            raise ErrorReadingRegister
        
        #Shift and mask out GLDRIVE bits */
        val = (val >> 3) & 0b00000011
    
        return val
        
    def setGestureLEDDrive(self, drive):
        """
            .. method:: setGestureLEDDrive(drive)
                
                Sets the LED drive current during gesture mode
                    +--------+--------------+
                    | Value  |  LED Current |
                    +========+==============+
                    |  0     |   100 mA     |
                    +--------+--------------+
                    |  1     |    50 mA     |
                    +--------+--------------+
                    |  2     |    25 mA     |
                    +--------+--------------+
                    |  3     |    12.5 mA   |
                    +--------+--------------+


             
                drive the value for the LED drive current
        """
        try:
            val = self.write_read(APDS9960_GCONF2, 1)[0]
        except:
            raise ErrorReadingRegister
        
    
        #Set bits in register to given value */
        drive &= 0b00000011
        drive = drive << 3
        val &= 0b11100111
        val |= drive
        
          #Write register value back into GCONF2 register
        try:       
            self._write_bytes(APDS9960_GCONF2,val)
        except:
           raise ErrorWritingRegister



    def getGestureWaitTime(self):
        """
            .. method: getGestureWaitTime
                Gets the time in low power mode between gesture detections
             
                    +----------+-------------+
                    |  Value   |  Wait time  |
                    +==========+=============+
                    |    0     |     0 ms    |
                    +----------+-------------+
                    |    1     |     2.8 ms  |
                    +----------+-------------+
                    |    2     |     5.6 ms  |
                    +----------+-------------+
                    |    3     |     8.4 ms  |
                    +----------+-------------+
                    |    4     |    14.0 ms  |
                    +----------+-------------+
                    |    5     |    22.4 ms  |
                    +----------+-------------+
                    |    6     |    30.8 ms  |
                    +----------+-------------+
                    |    7     |    39.2 ms  |
                    +----------+-------------+
             
                return the current wait time between gestures.
        """
        try:
            val = self.write_read(APDS9960_GCONF2, 1)[0]
        except:
            raise ErrorReadingRegister
    
        #Mask out GWTIME bits */
        val &= 0b00000111
    
        return val

    def setGestureWaitTime(self, time):
        """
            .. method:: setGestureWaitTime(time)
            
                Sets the time in low power mode between gesture detections

                    +----------+-------------+
                    |  Value   |  Wait time  |
                    +==========+=============+
                    |    0     |     0 ms    |
                    +----------+-------------+
                    |    1     |     2.8 ms  |
                    +----------+-------------+
                    |    2     |     5.6 ms  |
                    +----------+-------------+
                    |    3     |     8.4 ms  |
                    +----------+-------------+
                    |    4     |    14.0 ms  |
                    +----------+-------------+
                    |    5     |    22.4 ms  |
                    +----------+-------------+
                    |    6     |    30.8 ms  |
                    +----------+-------------+
                    |    7     |    39.2 ms  |
                    +----------+-------------+
             
                the value for the wait time
        """

        try:
            val = self.write_read(APDS9960_GCONF2, 1)[0]
        except:
            raise ErrorReadingRegister
    
        #Set bits in register to given value
        time &= 0b00000111
        val &= 0b11111000
        val |= time
    
        try:       
            self._write_bytes(APDS9960_GCONF2,val)
        except:
           raise ErrorWritingRegister



#*
#  * @brief Gets the low threshold for ambient light interrupts
#  *
#  * @param[out] threshold current low threshold stored on the APDS-9960
#  * @return True if operation successful. False otherwise.
#  */
    def getLightIntLowThreshold(self):
        """
            .. method:: getLightIntLowThreshold()
                
                Gets the low threshold for ambient light interrupts
                Return threshold current low threshold stored on the APDS-9960
                
        """
        
        try:
            valLow = self.write_read(APDS9960_AILTL, 1)[0]
            valHight = self.write_read(APDS9960_AILTH, 1)[0]
        except:
            raise ErrorReadingRegister
                    
        
        return valLow + (valHight << 8)

    

    def setLightIntLowThreshold(self, threshold):
        """
            .. method:: setLightIntLowThreshold(threshold)
            
                Sets the low threshold for ambient light interrupts
                threshold low threshold value for interrupt to trigger
        """
    
   
        #Break 16-bit threshold into 2 8-bit values */
        val_low = threshold & 0x00FF
        val_high = (threshold & 0xFF00) >> 8
        
        try:       
            self._write_bytes(APDS9960_AILTL,val_low)
        except:
           raise ErrorWritingRegister
  
        try:       
            self._write_bytes(APDS9960_AILTH,val_high)
        except:
           raise ErrorWritingRegister

 
  


    def getLightIntHighThreshold(self):
        """
            .. method:: getLightIntHighThreshold()
            
                Gets the high threshold for ambient light interrupts
                threshold: current low threshold stored on the APDS-9960
        """

           
        try:
            valLow = self.write_read(APDS9960_AIHTL, 1)[0]
            valHight = self.write_read(APDS9960_AIHTH, 1)[0]
        except:
            raise ErrorReadingRegister
                    
        
        return valLow + (valHight << 8)
        
  

    def setLightIntHighThreshold(self, threshold):
        """
            .. method:: setLightIntHighThreshold(threshold)
                
                Sets the low threshold for ambient light interrupts
                threshold low threshold value for interrupt to trigger
        """
    
   
        #Break 16-bit threshold into 2 8-bit values */
        val_low = threshold & 0x00FF
        val_high = (threshold & 0xFF00) >> 8
        
        try:       
            self._write_bytes(APDS9960_AIHTL,val_low)
        except:
           raise ErrorWritingRegister
  
        try:       
            self._write_bytes(APDS9960_AIHTH,val_high)
        except:
           raise ErrorWritingRegister



    def getProximityIntLowThreshold(self):
        """
            .. method:: getProximityIntLowThreshold()
                
                Gets the low threshold for proximity interrupts
            
        """
        
        try:
            val = self.write_read(APDS9960_PILT, 1)[0]
        except:
            raise ErrorReadingRegister
                    
        
        return val
   


    def setProximityIntLowThreshold(self, threshold):
        """
            .. method:: setProximityIntLowThreshold(threshold)
            
                Sets the low threshold for proximity interrupts
                threshold: low threshold value for interrupt to trigger
            
        """
        
        try:       
            self._write_bytes(APDS9960_PILT,threshold)
        except:
           raise ErrorWritingRegister

    
    def getProximityIntHighThreshold(self):
        
        """
            .. method:: getProximityIntHighThreshold()
                
               Gets the high threshold for proximity interrupts
            
        """
        
        try:
            val = self.write_read(APDS9960_PIHT, 1)[0]
        except:
            raise ErrorReadingRegister
                    
        
        return val
   

    def setProximityIntHighThreshold(self, threshold):
        """
            .. method:: setProximityIntHighThreshold(threshold)
                
                Sets the high threshold for proximity interrupts
                threshold: high threshold value for interrupt to trigger
            
        """
        
        try:       
            self._write_bytes(APDS9960_PIHT,threshold)
        except:
           raise ErrorWritingRegister


    def getAmbientLightIntEnable(self):
        """
            .. method:: getAmbientLightIntEnable()
                
                Gets if ambient light interrupts are enabled or not
                Return 1 if interrupts are enabled, 0 if not.
        """
        
        try:
            val = self.write_read(APDS9960_ENABLE, 1)[0]
        except:
            raise ErrorReadingRegister

        # Shift and mask out AIEN bit */
        val = (val >> 4) & 0b00000001
    
        return val



    def setAmbientLightIntEnable(self, enable):
        """
            .. method:: setAmbientLightIntEnable(enable)
                
                Turns ambient light interrupts on or off
                enable 1 to enable interrupts, 0 to turn them off
        """

        try:
            val = self.write_read(APDS9960_ENABLE, 1)[0]
        except:
            raise ErrorReadingRegister
   
 
        # Set bits in register to given value */
        enable &= 0b00000001
        enable = enable << 4
        val &= 0b11101111
        val |= enable
    
        try:       
            self._write_bytes(APDS9960_ENABLE,val)
        except:
           raise ErrorWritingRegister
   

    def getProximityIntEnable(self):
        """
            .. method:: getProximityIntEnable()
                
                Gets if proximity interrupts are enabled or not
                Return 1 if interrupts are enabled, 0 if not.
        """
        
        try:
            val = self.write_read(APDS9960_ENABLE, 1)[0]
        except:
            raise ErrorReadingRegister

   
        # Shift and mask out PIEN bit */
        val = (val >> 5) & 0b00000001
        
        return val


    def setProximityIntEnable(self, enable):
        """
            .. method:: setProximityIntEnable(enable)
            
                Turns proximity interrupts on or off
                enable 1 to enable interrupts, 0 to turn them off
        """

        try:
            val = self.write_read(APDS9960_ENABLE, 1)[0]
        except:
            raise ErrorReadingRegister
   
        # Set bits in register to given value */
        enable &= 0b00000001
        enable = enable << 5
        val &= 0b11011111
        val |= enable
        
        try:       
            self._write_bytes(APDS9960_ENABLE,val)
        except:
           raise ErrorWritingRegister
   

    def getGestureIntEnable(self):
        """
            .. method:: getGestureIntEnable()
            
                Gets if gesture interrupts are enabled or not
                return 1 if interrupts are enabled, 0 if not.
        """
        try:
            val = self.write_read(APDS9960_GCONF4, 1)[0]
        except:
            raise ErrorReadingRegister
    
   
    
        # Shift and mask out GIEN bit */
        val = (val >> 1) & 0b00000001
        
        return val


    def setGestureIntEnable(self, enable):

        """
            .. method:: setGestureIntEnable(enable)
            
                Turns gesture-related interrupts on or off
                enable 1 to enable interrupts, 0 to turn them off
        """

        try:
            val = self.write_read(APDS9960_GCONF4, 1)[0]
        except:
            raise ErrorReadingRegister
    
    
    
        # Set bits in register to given value */
        enable &= 0b00000001
        enable = enable << 1
        val &= 0b11111101
        val |= enable
    
        try:       
            self._write_bytes(APDS9960_GCONF4,val)
        except:
           raise ErrorWritingRegister
   

# #*
#  * @brief Clears the ambient light interrupt
#  *
#  * @return True if operation completed successfully. False otherwise.
#  */
    # def clearAmbientLightInt(self):

    # uint8_t throwaway
    # if not wireReadDataByte(APDS9960_AICLEAR, throwaway): 
    #     return False
    
    
    # return True


#*
 # * @brief Clears the proximity interrupt
 # *
 # * @return True if operation completed successfully. False otherwise.
 # */
 #    def clearProximityInt(self):

 #    uint8_t throwaway
 #    if not wireReadDataByte(APDS9960_PICLEAR, throwaway): 
 #        return False
    
    
 #    return True


#*
#  * @brief Tells if the gesture state machine is currently running
#  *
#  * @return 1 if gesture state machine is running, 0 if not. 0xFF on error.
#  */
#     def getGestureMode(self):

#     uint8_t val
    
#     # Read value from GCONF4 register */
#     if not wireReadDataByte(APDS9960_GCONF4, val): 
#         return ERROR
    
    
#     # Mask out GMODE bit */
#     val &= 0b00000001
    
#     return val


# #*

    def setGestureMode(self, mode):
        """
            .. method:: setGestureMode(mode)
            
                Tells the state machine to either enter or exit gesture state machine
                mode 1 to enter gesture state machine, 0 to exit.
                True if operation successful. False otherwise.
        """
        try:
            val = self.write_read(APDS9960_GCONF4, 1)[0]
        except:
            raise ErrorReadingRegister
            
        #Set bits in register to given value */
        mode &= 0b00000001;
        val &= 0b11111110;
        val |= mode;
    
             
        self._write_bytes(APDS9960_GCONF4, val)
        


    def _printDEBUG(self, *msg):
        if DEBUG:
            print(*msg)

    def _write_bytes(self,reg , val):
        try:   
            self.write_bytes(reg, val)
            sleep(100)
        except:
            raise ErrorWritingRegister
