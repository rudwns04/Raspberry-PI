import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀의 번호를 설정
button_pin = 3
buzzer_pin = 24

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)

pwm = GPIO.PWM(buzzer_pin, 1.0)  # 초기 주파수를 1Hz로 설정
pwm.start(0.0)  # 0으로 설정하여 꺼놓음

note_frequencies = {
    1: 262,
    2: 294,
    3: 330,
    4: 349,
    5: 392,
    6: 440,
    7: 494,
    8: 523,
}

def play_music(note):
    if note in note_frequencies:
        frequency = note_frequencies[note]
        pwm.start(10)  # PWM 시작
        pwm.ChangeFrequency(frequency)
        time.sleep(0.5)
        pwm.stop()  # PWM 정지
        time.sleep(0.5)

try:
    note_counter = 0
    while True:
        if GPIO.input(button_pin) == GPIO.LOW:
            time.sleep(0.1)
            while GPIO.input(button_pin) == GPIO.LOW:
                time.sleep(0.1)

            note_counter += 1
            if note_counter > 8:
                note_counter = 1

            play_music(note_counter)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()