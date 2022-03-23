#include <stdio.h>
#include <stdlib.h>

int main()
{
	const int NUM = 5;  //we can't change this value
	printf("%d\n",NUM);
	printf("Hello\n");  //this is also considered as constant
	printf("%d",70);  //70 also considered as constant
	
	return 0;
}
