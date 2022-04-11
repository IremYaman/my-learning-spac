#include <stdio.h>
#include <stdlib.h>

int main(){
	double firstNum;
	printf("Enter first number: ");
	scanf("%lf",&firstNum);
	
	char operator;
	printf("Enter operator(+,-,*,/): ");
	scanf(" %c",&operator);
	
	double secondNum;
	printf("Enter second number: ");
	scanf("%lf",&secondNum);
	
	if(operator == '+') {                            //TEK TIRNAK
		printf("= %f",firstNum + secondNum);
	} else if(operator == '-' ) {
		printf("= %f",firstNum - secondNum);
	} else if(operator == '*' ) {
	    printf("= %f",firstNum * secondNum);
	} else if(operator == '/' ) {
		printf("= %f",firstNum / secondNum);
	} else {
		printf("Something is wrong");
	}
	

	
	return 0;
}
