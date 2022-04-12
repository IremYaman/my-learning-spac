#include <stdio.h>
#include <stdlib.h>

struct Student {
	char name[50];
	char major[50];
	int age;
	double gpa;
	
};

int main() {
	
		struct Student student1;
		student1.age = 19;
		student1.gpa = 3.6;
		strcpy(student1.name, "İrem");
		strcpy(student1.major,"Spanish Language and Literature");
		
		struct Student student2;
		student2.age = 21;
		student2.gpa = 2.98;
		strcpy(student2.name,"Mert");
		strcpy(student2.major,"Computer Science");
		
		
		printf("%s",student1.major);
	
	return 0;
}
