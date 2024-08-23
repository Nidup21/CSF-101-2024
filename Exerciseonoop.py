class Dog:
    def __init__(self, name, color, age ):
        self.name = name
        self.color = color
        self.age = age

    def bark(self): 
        return f"The {self.name} is {self.age} old and has {self.color} fur "
    
#Creating objects (instance)
a = Dog("Nima", "black", "3 years")
b = Dog("Dawa", "brown", "1 years")
c = Dog("Karma", "red", "4 years")

#interacting with objects
print(c.bark())