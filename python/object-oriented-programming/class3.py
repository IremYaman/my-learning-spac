#class
class Circle:

    #class attribute
    pi = 3.14

    #constructor (yapıcı method)
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    #methods
    def perimeterCalculation(self):
        return 2* self.pi * self.radius

    
    def areaCalculation(self):
        return self.pi * (self.radius**2)

    def show(self):
        print(f"{self.name}: area: {self.areaCalculation()} perimeter: {self.perimeterCalculation()} ")

#object
c1 = Circle("c1", 4)

#accessing object attributes
c1.show()
    

