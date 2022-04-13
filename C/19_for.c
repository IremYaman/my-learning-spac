#include <stdio.h>
#include <stdlib.h>

int main() {
	
	/*
	int i=1;
	while( i<=5 ) {
		printf("%d\n",i);
		i++;
	}
	
	for(i=1; i<=5; i++) {
		printf("%d\n",i);
	}
	*/ 
	
	int luckyNumbers[] = {4,5,3,1,8};
	
	int i;
	for(i = 0; i<5; i++){
		printf("%d\n",luckyNumbers[i]);
	}
	return 0;
}
