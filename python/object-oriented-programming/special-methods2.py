# class Snowflake:
#     pass

# flake = Snowflake()
# print(dir(flake)) #prints the speacial methods available to use.

class Martian:
    pass 

m1 = Martian()
m1.first_name = "Owen"   #ANOTHER WAY TO ADD ATTRIBUTES
m1.last_name = "Phelps"
print(m1.__dict__)       #ANOTHER WAY TO USE SPECIAL METHODS


class Martian:
    """Someone who lives on Mars."""

    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name = ln
    def algo(self):
       print("algo unimportante")
    
    def __setattr__(self, name, value):  #method is called twice cause we assigned both first name and last name in init method.
        print(f">>> You set {name} = {value}")
        self.__dict__[name] = value

    def __getattr__(self,name):
        print(f">>> Get the '{name}' attribute ") #has to be ' not "
        if name == "full_name":
            return f"{self.first_name} {self.last_name}"
        else:
            raise AttributeError(f"No attribute named {name}")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# print(Martian.__doc__) 
# m = Martian("İrem", "Yaman") #both prints Someone who lives on Mars.
# print(m.__doc__)

# m = Martian("Mert", "Kuzu")
# print(m.__dict__) #we have to add the setts to dictionary ourselves bc we created our own sett attribute method.

# print(m.full_name)

m = Martian("Joey", "Tribbiani")
print(m)