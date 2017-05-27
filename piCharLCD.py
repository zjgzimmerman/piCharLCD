#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import binascii

# Interfacing a raspberry pi with a character LCD screen through GPIO

##########################################
# Character LCD Pinout                   #
# 01 - Ground                            #
# 02 - +5v                               #
# 03 - Contrast                          #
# 04 - Register select 0-Command 1-Data  #
# 05 - R/W 0-Write 1-Read                #
# 06 - Enable - execute command          #
# 07 - Data bit 0                        #
# 08 - Data bit 1                        #
# 09 - Data bit 2                        #
# 10 - Data bit 3                        #
# 11 - Data bit 4                        #
# 12 - Data bit 5                        #
# 13 - Data bit 6                        #
# 14 - Data bit 7 / Busy Flag            #
# 15 - Backlight Anode +                 #
# 16 - Backlight Cathode -               #
##########################################

class piCharLCD:
	rsPin = 0
	rwPin = 0
	enPin = 0
	rsVal, rwVal, enVal = 0
	dbPins = []
	dbVal = [0, 0, 0, 0, 0, 0, 0, 0]
	def __init__(self, rs, rw, en, dbPins):
		GPIO.setmode(GPIO.BCM)
		# GPIO pin numbers
		self.rsPin = rs # Register select
		self.rwPin = rw # read/write select
		self.enPin = en # Enable
		self.dbPins = dbPins # Data bit list (0-7)

		# Get GPIO pins ready
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(rsPin, GPIO.OUT)
		GPIO.setup(rwPin, GPIO.OUT)
		GPIO.setup(enPin, GPIO.OUT)
		for pin in dbPins:
			GPIO.setup(pin, GPIO.OUT)

	def enPulse():
		GPIO.output(enPin, True)
		time.sleep(1/1000) #Leave enable high for a millisecond
		GPIO.output(enPin, False)

	def isBusy():
		pass
		#Function to check state of DB7 to see if it is set to busy
		#Set RS to 0 and RW to 1, then get DB7 state
		GPIO.output(rsPin, False)
		GPIO.output(rwPin, True)

	#Returns list of 8 bits for ascii value of input
	def asciiToBin(char):
		outData = [x for x in bin(ord(char))[2:].zfill(8)]
		return outData

	def cleanup():
		GPIO.cleanup()
