#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>
#include <unistd.h>

// 사용할 GPIO 핀의 번호를 설정
#define BUZZER_PIN 5

// 4 옥타브: 도(0) / 레(1) / 미(2) / 파(3) / 솔(4) / 라(5) / 시(6) / 도(7) / 레(8) / 미(9) / 파(10) / 솔(11) / 라(12) / 시(13) / 도(14)
int scale[] = {262, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 784, 880, 968};

void play_music(int frequency) {
    softPwmWrite(BUZZER_PIN, 10);  // PWM 시작
    softPwmCreate(BUZZER_PIN, 0, 100);  // softPwm 초기화
    softPwmWrite(BUZZER_PIN, 10);  // PWM 시작
    delay(500);
    softPwmStop(BUZZER_PIN);  // PWM 정지
    delay(500);
}

int main() {
    char user_input;

    // GPIO 설정
    if (wiringPiSetup() == -1) {
        fprintf(stderr, "Unable to setup wiringPi.\n");
        return 1;
    }

    pinMode(BUZZER_PIN, OUTPUT);

    while (1) {
        printf("키를 입력하세요 (a: 도, s: 레, d: 미, f: 파, g: 솔, r: 라, I: 시, k: 도, Q: 종료): ");
        scanf(" %c", &user_input);

        if (user_input == 'a') {
            play_music(scale[0]);  // 도
        } else if (user_input == 's') {
            play_music(scale[1]);  // 레
        } else if (user_input == 'd') {
            play_music(scale[2]);  // 미
        } else if (user_input == 'f') {
            play_music(scale[3]);  // 파
        } else if (user_input == 'g') {
            play_music(scale[4]);  // 솔
        } else if (user_input == 'r') {
            play_music(scale[5]);  // 라
        } else if (user_input == 'I') {
            play_music(scale[6]);  // 시
        } else if (user_input == 'k') {
            play_music(scale[7]);  // 도
        } else if (user_input == 'Q' || user_input == 'q') {
            break;  // 프로그램 종료
        } else {
            printf("잘못된 입력입니다. 다시 시도하세요.\n");
        }
    }

    softPwmStop(BUZZER_PIN);  // PWM 정지
    return 0;
}
