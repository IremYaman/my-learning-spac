#include <stdio.h>
#include <stdlib.h>

int main() {
	
	/*
	int index = 1;
	while(index <=5) {
		printf("%d\n",index);
		index++;  //+1
	}
	*/
	
	int index = 6;
	do {
		printf("%d\n",index);   //does whatever is said first and then checks the condition
		index++;
	}while(index <= 5);
	
	return 0;
}
