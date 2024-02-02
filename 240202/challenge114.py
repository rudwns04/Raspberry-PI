import RPi.GPIO as GPIO
import time

# 모터 핀 세팅.
SERVO_PIN = 24

def set_servo_angle(angle):
    duty_cycle = (angle / 180.0) * 10.0 + 2.5
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)  # 안정화를 위한 대기시간

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# PWM 설정
pwm = GPIO.PWM(SERVO_PIN, 50)  # 주파수는 50Hz로 설정

# PWM 시작
pwm.start(0)

try:
    while True:
        user_input = input("키를 입력하세요 (q: 0도, w: 90도, e: 180도, Q: 종료): ")

        if user_input == 'q':
            set_servo_angle(0)
        elif user_input == 'w':
            set_servo_angle(90)
        elif user_input == 'e':
            set_servo_angle(180)
        elif user_input == 'Q':
            break  # 프로그램 종료
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

except KeyboardInterrupt:
    pass
finally:
    # PWM 정지 및 GPIO 리소스 정리
    pwm.stop()
    GPIO.cleanup()
