#include <wiringPi.h>
#include <stdio.h>
#include <unistd.h>

#define LED_PIN 4      // 라즈베리 파이의 4번 핀을 사용
#define BUTTON_PIN1 22

int ledStatus = 0;

void buttonCallback(void) {
    if (ledStatus) {
        // LED가 켜져 있으면 끄기
        digitalWrite(LED_PIN, LOW);
        ledStatus = 0;
    } else {
        // LED가 꺼져 있으면 켜기
        digitalWrite(LED_PIN, HIGH);
        ledStatus = 1;
    }
}

int main(void) {
    if (wiringPiSetup() == -1) {
        printf("wiringPi setup failed\n");
        return 1;
    }

    pinMode(BUTTON_PIN1, INPUT);
    pullUpDnControl(BUTTON_PIN1, PUD_UP);

    pinMode(LED_PIN, OUTPUT);

    wiringPiISR(BUTTON_PIN1, INT_EDGE_FALLING, &buttonCallback);

    while (1) {
        // 프로그램이 계속 실행되도록 유지
        usleep(100000);  // 0.1초 대기
    }

    return 0;
}
