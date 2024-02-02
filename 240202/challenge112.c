#include <wiringPi.h>
#include <stdio.h>

#define LED_PIN 4

int main(void) {
    wiringPiSetup();
    softPwmCreate(LED_PIN, 0, 100);  // GPIO 핀, 초기값, 범위

    char userInput;

    while (1) {
        printf("키를 입력하세요 (0: 0%%, 5: 50%%, t: 100%%, Q: 종료): ");
        scanf(" %c", &userInput);

        if (userInput == '0') {
            softPwmWrite(LED_PIN, 0);  // 0% 밝기
        } else if (userInput == '5') {
            softPwmWrite(LED_PIN, 50);  // 50% 밝기
        } else if (userInput == 't' || userInput == 'T') {
            softPwmWrite(LED_PIN, 100);  // 100% 밝기
        } else if (userInput == 'Q' || userInput == 'q') {
            break;  // 프로그램 종료
        } else {
            printf("잘못된 입력입니다. 다시 시도하세요.\n");
        }
    }

    return 0;
}
