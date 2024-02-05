import RPi.GPIO as GPIO
import threading
import time

# GPIO 핀 번호 설정
RED_PIN = 4
GREEN_PIN = 5
BLUE_PIN = 6

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# 빨간색 LED를 0.7초 주기로 깜빡이는 함수
def red_led_blink():
    while True:
        GPIO.output(RED_PIN, GPIO.HIGH)
        time.sleep(0.35)
        GPIO.output(RED_PIN, GPIO.LOW)
        time.sleep(0.35)

# 초록색 LED를 1.3초 주기로 깜빡이는 함수
def green_led_blink():
    while True:
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        time.sleep(0.65)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        time.sleep(0.65)

# 파란색 LED를 1.7초 주기로 깜빡이는 함수
def blue_led_blink():
    while True:
        GPIO.output(BLUE_PIN, GPIO.HIGH)
        time.sleep(0.85)
        GPIO.output(BLUE_PIN, GPIO.LOW)
        time.sleep(0.85)

# 메인 함수
def main():
    # 쓰레드 생성
    red_thread = threading.Thread(target=red_led_blink)
    green_thread = threading.Thread(target=green_led_blink)
    blue_thread = threading.Thread(target=blue_led_blink)

    # 쓰레드 시작
    red_thread.start()
    green_thread.start()
    blue_thread.start()

    try:
        # 메인 쓰레드가 종료될 때까지 대기
        red_thread.join()
        green_thread.join()
        blue_thread.join()

    except KeyboardInterrupt:
        # Ctrl+C를 눌렀을 때 GPIO 정리
        GPIO.cleanup()

if __name__ == "__main__":
    main()