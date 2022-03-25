#include <stdio.h>
#include <stdlib.h>

int main()
{
	char name[20];
	printf("Enter your name: ");
	scanf("%s",name);
	
	int age;
	printf("Enter your age: ");
	scanf("%d",&age);
	
	sayHi(name,age);
	
	return 0;
}

void sayHi(char name[],int age) {  //we use void when we don't want to return anything
	printf("Hi %s, you are %d. ",name,age);
}
