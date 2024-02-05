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
        user_input = input("키를 입력하세요 (q: 0도, w: 90도, e: 180도, Q: 종료): ")

        if user_input == 'q':
            StepCounter = 0
        elif user_input == 'w':
            StepCounter = 1
        elif user_input == 'e':
            StepCounter = 2
        elif user_input == 'Q':
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
            continue

        for _ in range(200):  
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
    print("\nExiting program.")
finally:
    GPIO.cleanup()