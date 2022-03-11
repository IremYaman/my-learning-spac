class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def info(self):
        print(f"name: {self.name} / surname: {self.surname} / age: {self.age} ")

    def whoAmI(self):
        print("I am a person. ")

class Student(Person):
    def __init__(self, name, surname,age,number):
        super().__init__(name,surname,age)
        self.number= number

    #override
    def whoAmI(self):
        print(f"I am a student and my school number is {self.number}. ")


p1 = Person("İrem", "Yaman", 19)
s1 = Student("Mert", "Kuzu",21,214410019)

p1.whoAmI()
s1.info()
s1.whoAmI()