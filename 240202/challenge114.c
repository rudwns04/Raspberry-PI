#include <wiringPi.h>
#include <stdio.h>

#define SERVO_PIN 24

void setServoAngle(int angle) {
    int pulseWidth = (angle * 1000 / 180) + 500;
    pwmWrite(SERVO_PIN, pulseWidth);
    delay(300);  // 안정화를 위한 대기시간
}

int main(void) {
    if (wiringPiSetup() == -1) {
        printf("WiringPi initialization failed\n");
        return 1;
    }

    pinMode(SERVO_PIN, PWM_OUTPUT);
    pwmSetMode(PWM_MODE_MS);
    pwmSetClock(192);
    pwmSetRange(2000);

    try {
        while (1) {
            char userInput;
            printf("키를 입력하세요 (q: 0도, w: 90도, e: 180도, Q: 종료): ");
            scanf(" %c", &userInput);

            switch (userInput) {
                case 'q':
                    setServoAngle(0);
                    break;
                case 'w':
                    setServoAngle(90);
                    break;
                case 'e':
                    setServoAngle(180);
                    break;
                case 'Q':
                case 'q':
                    return 0;  // 프로그램 종료
                default:
                    printf("잘못된 입력입니다. 다시 시도하세요.\n");
                    break;
            }
        }
    } catch (...) {
        // 예외 처리
    } finally {
        // PWM 정지 및 GPIO 리소스 정리
        pwmWrite(SERVO_PIN, 0);
        delay(300);
        pinMode(SERVO_PIN, INPUT);
    }

    return 0;
}
