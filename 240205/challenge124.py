import RPi.GPIO as GPIO
import time

# GPIO 설정
GPIO.setmode(GPIO.BCM)
StepPins = [16,17,18,19]
button_pin = 20  # 버튼을 GPIO 핀 20에 연결
for pin in StepPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)

GPIO.setup(button_pin, GPIO.IN)
    
StepCounter = 0

StepCount = 4

Seq = [[0,0,0,1],
       [0,0,1,0],
       [0,1,0,0],
       [1,0,0,0]]
       
button_press_count = 0       


try:
    while True:
        current_button_state = GPIO.input(button_pin)

        if current_button_state == GPIO.LOW and last_button_state == GPIO.HIGH:
            button_press_count += 1
            print(f"버튼을 {button_press_count}번 눌렀습니다.")

            target_angle = ((button_press_count - 1) % 3) * 90  # 3번 누를 때마다 초기화

            for _ in range(int(target_angle / 1.8)):  # 모터 및 원하는 속도에 맞게 스텝 수를 조절하세요
                for pin in range(4):
                    xpin = StepPins[pin]
                    if Seq[StepCounter][pin] != 0:
                        GPIO.output(xpin, True)
                    else:
                        GPIO.output(xpin, False)
                StepCounter += 1

                if StepCounter == StepCount:
                    StepCounter = 0
                if StepCounter < 0:
                    StepCounter = StepCount

                time.sleep(0.01)

            if button_press_count % 3 == 0:  # 3번 누를 때마다 출력 초기화
                button_press_count = 0

        last_button_state = current_button_state

except KeyboardInterrupt:
    print("\n프로그램을 종료합니다.")
finally:
    GPIO.cleanup()