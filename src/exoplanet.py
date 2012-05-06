#!/usr/bin/python

"""
kepler visualizer.
"""

import time
import serial
import pyfits
import math
import ConfigParser

def main():
        config = ConfigParser.RawConfigParser()
	config.read('settings.cfg')
	
	try:
		ser = serial.Serial(config.get('Device','usbserial'), 9600)
	
	except serial.serialutil.SerialException:
		print "Please check usb serilal device and update it in settings.cfg"
		exit()

	try:
		file = pyfits.open(config.get('Data','file'))

	except IOError:
		print "Please update correct path for fits file in settings.cfg"
		exit()
	
	#Read sap_flux value
	tbData = file[1].data
	sapFlux = tbData.field('SAP_FLUX')

	dataMin = min(sapFlux)
	dataMax = max(sapFlux)
        
        #Convert data to analog value 0-255 for use with arduino.
	for i in sapFlux:
		if math.isnan(i):
			pass
		else:
			var = (i - dataMin)/ (dataMax-dataMin)
        		analogVal = int(var * 255)
			ser.write(bytes(chr(analogVal)))
			time.sleep(0.03)
        		print analogVal
	
	file.close()
        analogVal = 0
        ser.write(bytes(chr(analogVal)))

if __name__ == "__main__":
    main()
