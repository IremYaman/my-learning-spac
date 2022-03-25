#include <stdio.h>
#include <stdlib.h>

double cube(double num) {  //we don't get any error if we write functions above main function
	return num*num*num;    //return breaks us out from the function so anything underneath will be untouched
}

//double cube(double num); //PROTOTYPE

int main()
{
	double num;
	printf("Enter a number: ");
	scanf("%lf",&num);
	printf("Answer: %f",cube(num));
	
	return 0;
}

/*
double cube(double num) {  //if we want to write the function blow the main funstion we need to PROTOTYPE the function 
	return num*num*num;
*/
