#include <wiringPi.h>
#include <stdio.h>

#define LED_PIN 4

int main(void) {
    wiringPiSetup();
    pinMode(LED_PIN, OUTPUT);

    char userInput;

    while (1) {
        printf("키를 입력하세요 (N: LED 켜기, F: LED 끄기, Q: 종료): ");
        scanf(" %c", &userInput);

        if (userInput == 'N' || userInput == 'n') {
            digitalWrite(LED_PIN, HIGH);  // LED 켜기
        } else if (userInput == 'F' || userInput == 'f') {
            digitalWrite(LED_PIN, LOW);   // LED 끄기
        } else if (userInput == 'Q' || userInput == 'q') {
            break;  // 프로그램 종료
        } else {
            printf("잘못된 입력입니다. 다시 시도하세요.\n");
        }
    }

    return 0;
}
