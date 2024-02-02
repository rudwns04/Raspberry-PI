import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정
led_pin = 4  # 라즈베리 파이의 4번 핀을 사용
button_pin1 = 22

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin1, GPIO.IN)

led_status = False

def button_callback(channel):
    global led_status
    if led_status:
        # LED가 켜져 있으면 끄기
        GPIO.output(led_pin, GPIO.LOW)
        led_status = False
    else:
        # LED가 꺼져 있으면 켜기
        GPIO.output(led_pin, GPIO.HIGH)
        led_status = True

GPIO.add_event_detect(button_pin1, GPIO.FALLING, callback=button_callback, bouncetime=300)

try:
    while True:
        # 프로그램이 계속 실행되도록 유지
        time.sleep(0.1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
