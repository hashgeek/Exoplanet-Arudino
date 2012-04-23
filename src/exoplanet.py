#!/usr/bin/python

"""
kepler visualizer.
"""

import time
import serial


def main():
	#values are hard coaded. Will use config file later.
	#ser = serial.Serial('/dev/ttyACM0', 9600)
	ser = serial.Serial('/dev/ttyUSB0', 9600)
	file = open("../data/flux.txt")
	data = []
	
	#Read sap_flux value
	while 1:
    		line = file.readline()
    		if not line:
        		break
    		try:
       			fluxVal = float(line)
       			data.append(fluxVal)
    		except ValueError:
       			pass

	dataMin = min(data)
	dataMax = max(data)
        
        #Convert data to analog value 0-255 for use with arduino.
	for i in data:
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
