import RPi.GPIO as GPIO

# GPIO 핀 번호 설정
led_pin = 4  # 라즈베리 파이의 0번 핀을 사용

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # 사용자로부터 입력 받기
        user_input = input("키를 입력하세요 (N: LED 켜기, F: LED 끄기, Q: 종료): ")

        # 입력에 따라 LED 켜고 끄기
        if user_input.upper() == 'N':
            GPIO.output(led_pin, GPIO.HIGH)  # LED 켜기
        elif user_input.upper() == 'F':
            GPIO.output(led_pin, GPIO.LOW)   # LED 끄기
        elif user_input.upper() == 'Q':
            break  # 프로그램 종료
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

except KeyboardInterrupt:
    pass
finally:
    # GPIO 리소스 정리
    GPIO.cleanup()
