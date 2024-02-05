import RPi.GPIO as GPIO
import threading
import time

# GPIO 핀 번호 설정
RED_PIN = 4
GREEN_PIN = 5

# 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

# 함수 정의 - 빨강색 LED를 0.7초 주기로 밝아지고 어두워지고 반복
def red_led_thread():
    while True:
        GPIO.output(RED_PIN, GPIO.HIGH)  # 빨강색 LED 켜기
        time.sleep(0.35)
        GPIO.output(RED_PIN, GPIO.LOW)   # 빨강색 LED 끄기
        time.sleep(0.35)

# 함수 정의 - 초록색 LED를 1.3초 주기로 밝아지고 어두워지고 반복
def green_led_thread():
    while True:
        GPIO.output(GREEN_PIN, GPIO.HIGH)  # 초록색 LED 켜기
        time.sleep(0.65)
        GPIO.output(GREEN_PIN, GPIO.LOW)   # 초록색 LED 끄기
        time.sleep(0.65)

# 메인 함수
def main():
    # 쓰레드 생성 및 시작
    red_thread = threading.Thread(target=red_led_thread)
    green_thread = threading.Thread(target=green_led_thread)

    red_thread.start()
    green_thread.start()

    # 메인 쓰레드에서 아무 동작이 없도록 대기
    red_thread.join()
    green_thread.join()

# 프로그램 실행
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Ctrl+C를 누르면 프로그램 종료
        GPIO.cleanup()