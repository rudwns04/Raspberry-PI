import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0) #초기 주파수를 1Hz로 설정
pwm.start(10.0) #듀티비를 90%로 높여 설정함(음 구분이 더 잘되고 조금 더 부드럽게 들림

# ==동요 : 반짝 반짝 작은별 계이름 ==
#도도솔솔라라솔파라미미레리도 솔솔파파미미레 솔솔파파미미레 도도솔솔라라솔 파파미미레레도

# 4 옥타브: 도(0) / 레(1) / 미(2) / 파(3) / 솔(4) / 라(5) / 시(6) / 도(7)/ 레(8) / 미(9) / 파(10) /솔(11) / 라(12) / 시(13) / 도(14)
scale = [262,294,330,349,392,440,494,523,587,659,698,784,880,968]
twinkle = [4,4,2,3,4,5,5,4,4,7,9,8,7,8, 
           9,9,8,8,7,8,7,5,5,4,4,4,2,1,0, 
           1,1,2,0,1,1,2,4,5,7,9,8,7,8,
           9,9,8,8,7,8,7,5,5,4,4,4,2,1,0]
try:
        for i in range(0, 60):
                pwm.ChangeFrequency(scale[twinkle[i]])
                if i==8:
                        time.sleep(1.0)
                if i==3 or i==4 or i==12 or i==13 or i==20 or i ==21 or i==28 or i==29 or i==42 or i ==43 or i==50 or i==51 or i==57 or i==58:
                        time.sleep(0.25)
                if i==14 or i==30 or i==44 or i==59:
                        time.sleep(1.0)       
                else:
                        time.sleep(0.5)
       

finally:
        pwm.stop()
        GPIO.cleanup()
