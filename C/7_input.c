#include <stdio.h>
#include <stdlib.h>


int main()
{
	/*
	int age;
	printf("Enter your age: ");
	scanf("%d",&age);                             //use & 
	printf("You are %d years old. ", age);
	*/
	
	/*
	double gpa;
	printf("Enter your GPA: ");
	scanf("%lf",&gpa);                            //%lf
	printf("Your GPA is %f.",gpa);
	*/
	
	/*
	char grade;
	printf("Enter your grade: ");
	scanf("%c",&grade);
	printf("Your grade is %c. ",grade)
	*/
	 
	char name[20];                                //we need to specify how many charecters of input we can get
	printf("Enter your name: ");
	//scanf("%s",name);                           //no need to use &  //scanf only takes characters till space
	fgets(name,20,stdin);                         //this function only gets string of characters but you can get the whole input even if it includes space somewhere  //need to specify the amount of characters that can be input
	printf("Your name is %s. ",name);	          //after getting an input by fgets and printing it, the text after the input starts in a new line
	
	return 0;
}
