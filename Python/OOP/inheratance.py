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