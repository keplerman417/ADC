#!/usr/bin/env python
#
# Last Change: Sun Feb 04, 2018 at 09:04 PM -0500
# Author: Rohan Rajagopalan

from __future__ import absolute_import, division, print_function, unicode_literals
import time
import os
import unicodedata

try:
    from ADCPi import ADCPi
except ImportError:
    from bUrnIn.ADC.ADCPi import ADCPi


def main():
    '''
    Main program function
    '''
    start_time = time.time()
    adc = ADCPi(0x6E, 0x6F, 12)
    while True:

        # clear the console
        os.system('clear')

        # python dictionary (Channel: [adc_voltage, time])
        collect = {'ADC Channel 1':[], 'ADC Channel 2':[],
                   'ADC Channel 3':[], 'ADC Channel 4':[],
                   'ADC Channel 5':[], 'ADC Channel 6':[],
                   'ADC Channel 7':[], 'ADC Channel 8':[], 
                   'ADC Channel 9':[], 'ADC Channel 10':[],
                   'ADC Channel 11':[], 'ADC Channel 12':[],
                   'ADC Channel 13':[], 'ADC Channel 14':[],
                   'ADC Channel 15':[], 'ADC Channel 16':[],
                   'ADC Channel 17':[], 'ADC Channel 18':[],
                   'ADC Channel 19':[], 'ADC Channel 20':[],
                   'ADC Channel 21':[], 'ADC Channel 22':[],
                   'ADC Channel 23':[], 'ADC Channel 24':[],
                   'ADC Channel 25':[], 'ADC Channel 26':[],
                   'ADC Channel 27':[], 'ADC Channel 28':[],
                   'ADC Channel 29':[], 'ADC Channel 30':[],
                   'ADC Channel 31':[], 'ADC Channel 32':[],}

        # read from adc channels and print to screen
        # collects data from each ADC read and stores in dictionary
        print("ADC Channel 1: %02f" % adc.read_voltage(1))
        collect['ADC Channel 1'].append(adc.read_voltage(1))
        collect['ADC Channel 1'].append(time.time()-start_time)

        print("ADC Channel 2: %02f" % adc.read_voltage(2))
        collect['ADC Channel 2'].append(adc.read_voltage(2))
        collect['ADC Channel 2'].append(time.time()-start_time)

        print("ADC Channel 3: %02f" % adc.read_voltage(3))
        collect['ADC Channel 3'].append(adc.read_voltage(3))
        collect['ADC Channel 3'].append(time.time()-start_time)

        print("ADC Channel 4: %02f" % adc.read_voltage(4))
        collect['ADC Channel 4'].append(adc.read_voltage(4))
        collect['ADC Channel 4'].append(time.time()-start_time)

        print("ADC Channel 2: %02f" % adc.read_voltage(5))
        collect['ADC Channel 5'].append(adc.read_voltage(5))
        collect['ADC Channel 5'].append(time.time()-start_time)

        print("ADC Channel 6: %02f" % adc.read_voltage(6))
        collect['ADC Channel 6'].append(adc.read_voltage(6))
        collect['ADC Channel 6'].append(time.time()-start_time)

        print("ADC Channel 7: %02f" % adc.read_voltage(7))
        collect['ADC Channel 7'].append(adc.read_voltage(7))
        collect['ADC Channel 7'].append(time.time()-start_time)

        print("ADC Channel 8: %02f" % adc.read_voltage(8))
        collect['ADC Channel 8'].append(adc.read_voltage(8))
        collect['ADC Channel 8'].append(time.time()-start_time)
        
        print("ADC Channel 9: %02f" % adc.read_voltage(8))
        collect['ADC Channel 9'].append(adc.read_voltage(8))
        collect['ADC Channel 9'].append(time.time()-start_time)
        
        print("ADC Channel 10: %02f" % adc.read_voltage(8))
        collect['ADC Channel 10'].append(adc.read_voltage(8))
        collect['ADC Channel 10'].append(time.time()-start_time)
        
        #print (collect)

        #CTRL + C to end program
        # wait 0.2 seconds before reading the pins again
        time.sleep(0.2)

if __name__ == "__main__":
    main()
