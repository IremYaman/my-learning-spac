class Pet:
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old. ")


    def speak(self):
        print("I don't know what i say. ")


class Cat(Pet):
    def __init__(self, name, age, color ):
        super().__init__(name,age)
        self.color = color

    
    def speak(self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass



p1 = Pet("Lilac", 8)
p1.show()

        