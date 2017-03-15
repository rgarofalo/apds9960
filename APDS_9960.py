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

class APDS9960 (i2c.I2C):
 
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
    REG_ID      = 0x92
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
 
    # Congiguration register 2
    CONFIG2_LEDBOOST_150 = (1 << 4) # LED boost 150%
    CONFIG2_LEDBOOST_200 = (2 << 4) # LED boost 300%
    CONFIG2_LEDBOOST_300 = (3 << 4) # LED boost 300%
 
    GCONFIG3_GDIMS_LR = 2
    GCONFIG3_GDIMS_UD = 1 # 01
    GCONFIG4_GMODE = 1 # Gesture mode
 
    def __init__(self, i2cdrv, addr=APDS9960_I2CADDR, clk=100000):
        i2c.I2C.__init__(self,i2cdrv,addr,clk)
        self._addr = addr
        self._oss = 0
 
 
    def initialize(self):
        if (self.get_device_id() != 0xAB):
            return False
        self.write_byteswrite_bytes(self.REG_ENABLE)
        self.write_bytes(self.ENABLE_PON | self.ENABLE_PEN | self.ENABLE_GEN)
        self.write_bytes(self.REG_CONFIG2)
        self.write_bytes(self.CONFIG2_LEDBOOST_300)
        self.write_bytes(self.REG_GOFFSET_U, 70)
        self.write_bytes(self.REG_GOFFSET_D, 0)
        self.write_bytes(self.REG_GOFFSET_L, 10)
        self.write_bytes(self.REG_GOFFSET_R, 34)
        self.write_bytes(self.REG_CONFIG3, self.GCONFIG3_GDIMS_UD | self.GCONFIG3_GDIMS_LR)
        self.write_bytes(self.REG_GCONFIG4, self.GCONFIG4_GMODE)
 
    def get_device_id(self):
        return self.read(self.REG_ID)
 
    def gesture(self):
        level = self.read(self.REG_GFLVL)
        if (level == 0):
            return # no data
        fifo_u = self.read(self.REG_GFIFO_U)
        fifo_d = self.read(self.REG_GFIFO_D)
        fifo_l = self.read(self.REG_GFIFO_L)
        fifo_r = self.read(self.REG_GFIFO_R)
        
        return fifo_u, fifo_d, fifo_l, fifo_r
