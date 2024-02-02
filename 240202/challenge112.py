import RPi.GPIO as GPIO

# GPIO 핀 번호 설정
led_pin = 4  # 라즈베리 파이의 1번 핀을 사용

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

# PWM 객체 생성 (핀번호, 주파수)
pwm_led = GPIO.PWM(led_pin, 1000)  # 주파수는 1000Hz로 설정

try:
    pwm_led.start(0)  # 초기 duty cycle을 0으로 설정

    while True:
        # 사용자로부터 입력 받기
        user_input = input("키를 입력하세요 (0: 0%, 5: 50%, t: 100%, Q: 종료): ")

        # 입력에 따라 LED 밝기 조절
        if user_input == '0':
            pwm_led.ChangeDutyCycle(0)  # 0% 밝기
        elif user_input == '5':
            pwm_led.ChangeDutyCycle(50)  # 50% 밝기
        elif user_input == 't':
            pwm_led.ChangeDutyCycle(100)  # 100% 밝기
        elif user_input.upper() == 'Q':
            break  # 프로그램 종료
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

except KeyboardInterrupt:
    pass
finally:
    pwm_led.stop()  # PWM 정지
    GPIO.cleanup()
