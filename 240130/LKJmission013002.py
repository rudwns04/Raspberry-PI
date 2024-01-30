import RPi.GPIO as GPIO
import time

led_pin = 4 # 0 for WiringPi

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, 100) #channel=led_pin frequency=100Hz
pwm.start(0)

try:
	while True :
		print("1. LED 켜기")
		print("2. LED 끄기")
		print("3. LED 3초간 점점 밝기")
		print("4. LED 3초간 점점 어둡기")
		print("5. LED 3초간 점점 밝아지다가 3초간 점점 어둡기")
		print("6. 원하는 초 입력하면 입력된 초 동안 점점 밝아지다가 어두워지기")
		print("0. 프로그램 종료")
        
		choice = int(input("원하는 기능: "))
        
		if choice == 1:
			pwm.ChangeDutyCycle(100)
			print("LED ON")
		if choice == 2:
			pwm.ChangeDutyCycle(0)
			print("LED OFF")
		if choice == 3:
			for t_high in range(1,101,3):
				pwm.ChangeDutyCycle(t_high)
				time.sleep(0.01)
			print("LED ON")
		if choice == 4:
			for t_high in range(100, -1, -3):
				pwm.ChangeDutyCycle(t_high)
				time.sleep(0.01)
			print("LED OFF")
		if choice == 5:
			for t_high in range(1,101,3):
				pwm.ChangeDutyCycle(t_high)
				time.sleep(0.01)
			for t_high in range(100, -1, -3):
				pwm.ChangeDutyCycle(t_high)
				time.sleep(0.01)
			print("LED ON \nLED OFF")
		if choice == 6:
			custom_duration = int(input("원하는 초를 입력하세요: "))
			step_count = 100
			sleep_time = custom_duration / (2 * step_count)

			for t_high in range(0, 101, 1):
				pwm.ChangeDutyCycle(t_high)
				time.sleep(sleep_time)
			print("LED ON")
			for t_high in range(100, -1, -1):
				pwm.ChangeDutyCycle(t_high)
				time.sleep(sleep_time)
			print("LED OFF")
		if choice == 0:
			break
		else :
			print("올바른 번호를 입력하세요.")
	
except KeyboardInterrupt:
	pass
    
pwm.stop()
GPIO.cleanup()
