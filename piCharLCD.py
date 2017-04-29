#!/usr/bin/python3
import RPi.GPIO as GPIO

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
	def __init__(self, rs, rw, en, db):
		# GPIO pin numbers
		self.rs = rs # Register select
		self.rw = rw # read/write select
		self.en = en # Enable
		self.db = db # Data bit list (0-7)

		# Get GPIO pins ready
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(rs, GPIO.OUT)
		GPIO.setup(rw, GPIO.OUT)
		GPIO.setup(en, GPIO.OUT)
		for pin in db:
			GPIO.setup(pin, GPIO.OUT)

	def cleanup():
		GPIO.cleanup()
