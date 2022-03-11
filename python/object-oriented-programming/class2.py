#class
class Person:
    #class attributes
    address = "*Unknown*"

    #constructor(yapıcı method)
    def __init__(self, name, year):

        #object attributes
        self.name = name
        self.year = year

    #instance methods
    def describe(self):
        print(f"Hello, my name is {self.name} and i was born in {self.year}. I live in {self.address}. ")
    

    def calculateAge(self):
        return 2022 - self.year


#object (instance)
p1 = Person("Ali", 1990)
p2 = Person("Ayşe", 1988)

#updating
p1.name = "Ahmet"
p2.year = 2000
p1.address = "Ankara"

#accessing object attributes
p1.describe()
    #or
print(f"Hello, my name is {p1.name} and i was born in {p1.year}. I live in {p1.address}. ")
    #or
print(f"my name: {p2.name}, my age: {p2.calculateAge()}")