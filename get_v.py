#!/usr/bin/python3

import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1015(i2c)

#Single Ended Mode
for port in [ADS.P1, ADS.P2 ]:
    chan = AnalogIn(ads, port)
    adj = float(chan.voltage)/0.09

    print("voltage" + str(port) + ": %.2f" % adj)


    # print("port: " + str(port))
    # print("-------------")
    # print("value: " + str(chan.value))
    # print("voltage: " + str(chan.voltage))
    # # print(chan.value, chan.voltage)
    # print("adjusted value: " + str(adj) )
    # print("\n")







###################################

# Differential Mode
# chan = AnalogIn(ads, ADS.P0, ADS.P1)
# print(chan.value, chan.voltage)
