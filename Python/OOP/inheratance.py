class Vehicle:
    color = "white"
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def info(self):
        return f"{self.brand} moving at {self.speed} km/h"

class Car(Vehicle):
    def __init__(self, brand, speed, model):
        super().__init__(brand, speed)  # calls Vehicle.__init__ using super(), instead of rewriting the same __init__ code
        self.model = model

    def info(self):
        base = super().info()  # calls Vehicle.info()
        return f"{base}, model: {self.model}"

car1 = Car("Toyota", 120, "Corolla")
print(car1.info())

# Animal Class Representation with method overriding

"""class Animal:
    number_of_animals = 0
    def __init__(self, type, name):
        self.type = type
        self.name = name
        Animal.number_of_animals += 1

    def speak(self):
        return "Some sound!" 

class Dog(Animal):
    def __init__(self, type, name):
        super().__init__(type, name)          

    def speak(self) :
        return f"Woof! I'm {self.name}"       

class Cat(Animal):
    def __init__(self, type, name):
        super().__init__(type, name)

    def speak(self):
        return f"Meow, I'm {self.name}"   

dog1 = Dog("labrador", "Kitt")  
print(dog1.speak())       
"""