import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

while 1:
    if GPIO.input(27):
        print ("Detected")
        GPIO.output(buzzer, GPIO.HIGH)
        time.sleep(0.1)  # 부저를 2초 동안 울림
            
        # 부저 멈추기
        GPIO.output(buzzer, GPIO.LOW)
    else:
        print ("Not Detected")
    time.sleep(0.5)

GPIO.cleanup()