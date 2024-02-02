import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀의 번호를 설정
buzzer = 24

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0) #초기 주파수를 1Hz로 설정
pwm.start(0.0) #0으로 설정하여 꺼놓음

def play_music(frequency):
    pwm.start(10)  # PWM 시작
    pwm.ChangeFrequency(frequency)  
    time.sleep(0.5)
    pwm.stop()   # PWM 정지
    time.sleep(0.5)


# 4 옥타브: 도(0) / 레(1) / 미(2) / 파(3) / 솔(4) / 라(5) / 시(6) / 도(7)/ 레(8) / 미(9) / 파(10) /솔(11) / 라(12) / 시(13) / 도(14)
scale = [262,294,330,349,392,440,494,523,587,659,698,784,880,968]

try:
    while True:
        user_input = input("키를 입력하세요 (a: 도, s: 레, d: 미, f: 파, g: 솔, r: 라, I: 시, k: 도, Q: 종료): ")

        if user_input == 'a':
            play_music(262)           # 도
        elif user_input == 's':
            play_music(294)           # 레
        elif user_input == 'd':
            play_music(330)           # 미
        elif user_input == 'f':
            play_music(349)           # 파
        elif user_input == 'g':
            play_music(392)           # 솔
        elif user_input == 'r':
            play_music(440)           # 라
        elif user_input == 'I':
            play_music(494)           # 시
        elif user_input == 'k':
            play_music(523)           # 도
        elif user_input == 'Q':
            break  # 프로그램 종료
        elif user_input == 'q':
            break  # 프로그램 종료
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

finally:
        GPIO.cleanup()
