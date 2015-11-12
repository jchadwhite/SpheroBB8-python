#!/usr/bin/python
from bluepy import btle
import struct
import time
import BB8_driver
import sys
bb8 = BB8_driver.Sphero()
bb8.connect()
bb8.set_raw_data_strm(40, 1 , 0, False)

bb8.start()
time.sleep(2)
bb8.set_rgb_led(255,0,0,0,False)
time.sleep(1)
bb8.set_rgb_led(0,255,0,0,False)
time.sleep(1)
bb8.set_rgb_led(0,0,255,0,False)
time.sleep(3)
bb8.join()
bb8.disconnect()
sys.exit(1)

