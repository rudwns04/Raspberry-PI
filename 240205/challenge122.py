import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정
button_pin = 22  # 라즈베리 파이의 22번 핀을 사용
led_pin = 4     # 라즈베리 파이의 4번 핀을 사용

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

# PWM 객체 생성 (핀번호, 주파수)
pwm_led = GPIO.PWM(led_pin, 1000)  # 주파수는 1000Hz로 설정

# LED 초기화
pwm_led.start(0)
current_duty_cycle = 0  # 현재 duty cycle을 추적하기 위한 변수 추가

try:
    while True:
        # 버튼 입력 확인
        button_state = GPIO.input(button_pin)

        if button_state == GPIO.LOW:
            print("버튼 눌림")

            # LED 밝기 조절
            if current_duty_cycle == 0:
                print("LED 밝기: 0%")
                pwm_led.ChangeDutyCycle(0)
                current_duty_cycle = 50
            elif current_duty_cycle == 50:
                print("LED 밝기: 50%")
                pwm_led.ChangeDutyCycle(50)
                current_duty_cycle = 100
            elif current_duty_cycle == 100:
                print("LED 밝기: 100%")
                pwm_led.ChangeDutyCycle(100)
                current_duty_cycle = 0

            # 버튼 입력 디바운스
            time.sleep(0.2)

except KeyboardInterrupt:
    pass
finally:
    pwm_led.stop()  # PWM 정지
    GPIO.cleanup()