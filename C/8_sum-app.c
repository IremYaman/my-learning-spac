#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{	
	printf("SUMMING APP\n");
	double firstNumber;
	double secondNumber;
	printf("Enter the first number: ");
	scanf("%lf",&firstNumber);
    printf("Enter the second number: ");
    scanf("%lf",&secondNumber);
    printf("Result: %f",firstNumber + secondNumber);
    
	return 0;
}
