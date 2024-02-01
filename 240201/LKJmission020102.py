import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀의 번호를 설정
led_red = 4
led_green = 5
led_blue = 6
buzzer = 18
button_pin1 = 22
button_pin2 = 23
button_pin3 = 24
button_pin4 = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #핀모드 설정

# 버튼 핀의 입력설정
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_blue, GPIO.OUT)
GPIO.setup(button_pin1, GPIO.IN)
GPIO.setup(button_pin2, GPIO.IN)
GPIO.setup(button_pin3, GPIO.IN)
GPIO.setup(button_pin4, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0) #초기 주파수를 1Hz로 설정
pwm.start(0.0) #0으로 설정하여 꺼놓음

# 4 옥타브: 도(0) / 레(1) / 미(2) / 파(3) / 솔(4) / 라(5) / 시(6) / 도(7)/ 레(8) / 미(9) / 파(10) /솔(11) / 라(12) / 시(13) / 도(14)
scale = [262,294,330,349,392,440,494,523,587,659,698,784,880,968]


def play_music1():
    twinkle = [4,4,2,3,4,5,5,4,4,7,9,8,7,8, 
               9,9,8,8,7,8,7,5,5,4,4,4,2,1,0, 
               1,1,2,0,1,1,2,4,5,7,9,8,7,8,
               9,9,8,8,7,8,7,5,5,4,4,4,2,1,0]
               
    try :
        for i in range(0, 60):
            pwm.ChangeFrequency(scale[twinkle[i]])
            if i==8:
                time.sleep(1.0)
            if i==3 or i==4 or i==12 or i==13 or i==20 or i ==21 or i==28 or i==29 or i==42 or i ==43 or i==50 or i==51 or i==57 or i==58:
                time.sleep(0.25)
            if i==14 or i==30 or i==44 or i==59:
                time.sleep(1.0)   
            if GPIO.input(button_pin4) == GPIO.LOW:
                pwm.stop()
                return
            else:
                time.sleep(0.5)
    finally:
        pwm.stop()

def play_music2():
    twinkle = [0, 0, 4, 4, 5, 5, 4, 3, 3, 2, 2, 1, 1, 0, \
           4, 4, 3, 3, 2, 2, 1, 4, 4, 3, 3, 2, 2, 1, \
           0, 0, 4, 4, 5, 5, 4, 3, 3, 2, 2, 1, 1, 0]
               
    try :
        for i in range(0, 42):
            pwm.ChangeFrequency(scale[twinkle[i]])
            if i==6 or i==13 or i==20 or i==27 or i ==34 or i==41:
                time.sleep(1.0)
            if GPIO.input(button_pin4) == GPIO.LOW:
                pwm.stop()
                return
            else:
                time.sleep(0.5)
    finally:
        pwm.stop()
        
def play_music3():
    twinkle = [0,3,4,5,4,5,6,5,3,4,3,1,0, \
                0,3,4,5,4,3,4,5,3,4,1,2,3, \
                4,4,4,3,4,5,3,8,8,7,5,4 \
               ]
               
    try :
        for i in range(0, 40):
            pwm.ChangeFrequency(scale[twinkle[i]])
            if i==8 or i==21 or i==36 or i==38:
                time.sleep(1.0)
            if i==7 or i==13 or i==20 or i==26 or i ==35 or i==40:
                time.sleep(2.5)
            if GPIO.input(button_pin4) == GPIO.LOW:
                pwm.stop()
                return
            else:
                time.sleep(0.5)
    finally:
        pwm.stop()

def turn_on_led(color):
    if color == 'red':
        GPIO.output(led_red, GPIO.HIGH)
        GPIO.output(led_green, GPIO.LOW)
        GPIO.output(led_blue, GPIO.LOW)
    elif color == 'green':
        GPIO.output(led_red, GPIO.LOW)
        GPIO.output(led_green, GPIO.HIGH)
        GPIO.output(led_blue, GPIO.LOW)
    elif color == 'blue':
        GPIO.output(led_red, GPIO.LOW)
        GPIO.output(led_green, GPIO.LOW)
        GPIO.output(led_blue, GPIO.HIGH)
        
def turn_off_led():
    GPIO.output(led_red, GPIO.LOW)
    GPIO.output(led_green, GPIO.LOW)
    GPIO.output(led_blue, GPIO.LOW)

try:
    while True:
        if GPIO.input(button_pin1) == GPIO.LOW:
            print("Button 1 pushed!")
            turn_on_led('red')
            pwm.start(10.0)
            play_music1()
            turn_off_led()
            current_music = 'red'
        if GPIO.input(button_pin2) == GPIO.LOW:
            print("Button 2 pushed!")
            turn_on_led('green')
            pwm.start(10.0)
            play_music2()
            turn_off_led()
            current_music = 'green'
        if GPIO.input(button_pin3) == GPIO.LOW:
            print("Button 3 pushed!")
            turn_on_led('blue')
            pwm.start(10.0)
            play_music3()
            turn_off_led()
            current_music = 'blue'
        if GPIO.input(button_pin4) == GPIO.LOW:
            print("Button 4 pushed!")
            turn_off_led()
            pwm.stop()
            GPIO.cleanup()
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(led_red, GPIO.OUT)
            GPIO.setup(led_green, GPIO.OUT)
            GPIO.setup(led_blue, GPIO.OUT)
            GPIO.setup(button_pin1, GPIO.IN)
            GPIO.setup(button_pin2, GPIO.IN)
            GPIO.setup(button_pin3, GPIO.IN)
            GPIO.setup(button_pin4, GPIO.IN)
            GPIO.setup(buzzer, GPIO.OUT)
            pwm = GPIO.PWM(buzzer, 1.0)
            pwm.start(0.0)
            
        time.sleep(0.5)
    
    
finally:
        pwm.stop()
        GPIO.cleanup()
