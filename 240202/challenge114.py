import RPi.GPIO as GPIO
import time

# GPIO 설정
GPIO.setmode(GPIO.BCM)
StepPins = [16,17,18,19]

for pin in StepPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)
    
StepCounter = 0  

StepCount = 4

Seq = [[0,0,0,1],
       [0,0,1,0],
       [0,1,0,0],
       [1,0,0,0]]
       
try:
    while True:
        key_input = input("키를 입력하세요 (q: 0도, w: 90도, e: 180도, Q: 종료):")

        if key_input == 'q':
            target_angle = 0
        elif key_input == 'w':
            target_angle = 90
        elif key_input == 'e':
            target_angle = 180
        elif key_input == 'Q':
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
            continue

        for _ in range(int(target_angle / 0.18)):
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

except KeyboardInterrupt:
    print("\n프로그램을 종료합니다.")
finally:
    GPIO.cleanup()