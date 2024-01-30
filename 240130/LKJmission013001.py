import RPi.GPIO as GPIO
import time

led_red = 4
led_green = 5
led_blue = 6

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_blue, GPIO.OUT)


try:
	i=0
	while i<20 :
		i=i+1
		GPIO.output(led_red, True)
		print("RED LED On !! \n");
		time.sleep(0.5)
		GPIO.output(led_red, False)
		print("RED LED OFF !! \n");
		time.sleep(0.5)
		GPIO.output(led_green, True)
		print("GREEN LED On !! \n");
		time.sleep(0.5)
		GPIO.output(led_green, False)
		print("GREEN LED OFF !! \n");
		time.sleep(0.5)
		GPIO.output(led_blue, True)
		print("BLUE LED ON !! \n");
		time.sleep(0.5)
		GPIO.output(led_blue, False)
		print("BLUE LED OFF !! \n");
		time.sleep(0.5)
	
except KeyboardInterrupt:
	pass
GPIO.cleanup()
