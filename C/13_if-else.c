#include <stdio.h>
#include <stdlib.h>


int max(num1,num2,num3)
{
	int result; 
	if(num1>=num2 && num1>=num3) {             //&& means and
		result= num1;
	} else if(num2>=num1 && num2>=num3) {      //need to write else if
		result= num2;
	} else {
		result= num3;
	}
	return result;
}

int main()
{
	int num1;
	printf("Enter the first number: ");
	scanf("%d",&num1);
	
	int num2;
	printf("Enter the second number: ");
	scanf("%d",&num2);
	
	int num3;
	printf("Enter the third number: ");
	scanf("%d",&num3);
	
	printf("%d is the biggest.",max(num1,num2,num3));
	
	return 0;
}


/*
int main()
{
	if(3>4 || 2>1) {                           //|| means or
		printf("True\n");   
	} if(2==2) {         
		printf("Equal\n");
	} if(3!=2) {
		printf("Not equal\n");
	} if(!(2>3)) {                             //! here reverses the True False value
		printf("False");
	}
	
	return 0;
}
*/
