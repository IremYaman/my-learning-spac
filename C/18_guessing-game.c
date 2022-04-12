#include <stdio.h>   
#include <stdlib.h>     

int main() {
	
	int secretNumber;
    srand(time(NULL));
    secretNumber = rand() % 10;
	int guess;
	
	int index = 3;
	while(index > 0) {
		
		printf("Guess a number between 1-10: ");
		scanf("%d", &guess);
	
		if(secretNumber == guess){
			printf("Good job, you win!\n");
			break;
		}else if(secretNumber != guess){
			printf("Wrong guess.\n");
			index--;
			if(index == 0) {
				printf("You lost. ");
			}
		}	
	}
	
	return 0;
}
