import json
import threading
import time

try:
    import RPi.GPIO as GPIO
    """This is trapped so you can still run without RPi.GPIO
    GPIO will be checked before use
    """
    pi_interface = True
except:
    pi_interface = False
    pass

GPIO_STATE = {}

GPIO_ON = {}

def set(key,value):
	GPIO_STATE[key] = value
	if (key == "GPIO1") and pi_interface:
		if value.uppper() == "ON":
			GPIO.output(6,GPIO.HIGH)
		else:
			GPIO.output(6,GPIO.LOW)

	if (key == "GPIO2") and pi_interface:
		if value.uppper() == "ON":
			GPIO.output(13,GPIO.HIGH)
		else:
			GPIO.output(13,GPIO.LOW)

	if (key == "GPIO3") and pi_interface:
		if value.uppper() == "ON":
			GPIO.output(19,GPIO.HIGH)
		else:
			GPIO.output(19,GPIO.LOW)

	if (key == "GPIO4") and pi_interface:
		if value.uppper() == "ON":
			GPIO.output(26,GPIO.HIGH)
		else:
			GPIO.output(26,GPIO.LOW)
	if key in GPIO_ON:
		GPIO_ON[key]()
