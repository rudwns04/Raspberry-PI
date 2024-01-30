#include <wiringPi.h>
#include <stdio.h>

#define led_pin 7

int main(void){
	int i;
	
	if(wiringPiSetup() == -1)
		return 1;
	pinMode(led_pin, OUTPUT);
	while(1){
	digitalWrite(led_pin, HIGH);
	delay(1);
	digitalWrite(led_pin, LOW);
	delay(9);
	}
	
	return 0;
}
