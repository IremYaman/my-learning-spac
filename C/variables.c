#include <stdio.h>
#include <stdlib.h>

int main()
{
	char characterName[]= "George";
	int characterAge = 70;
	printf("There was once a man named %s\n",characterName);
	printf("He was %d years old\n", characterAge);
	
	characterAge = 80;
	printf("He really liked the name %s\n",characterName);
	printf("But did not like being %d\n",characterAge);
	/* 
	%c => single character
	%f => float
	%s => string
	%d => integer
	*/
	
	return 0;
}
