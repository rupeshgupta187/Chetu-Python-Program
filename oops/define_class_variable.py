# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
class Vehicle:
    color="white"
    def __init__(self, name,speed,milage):
        self.name=name
        self.speed=speed
        self.milage=milage
class Car(Vehicle):
    pass

class Bus(Vehicle):
    pass

bus=Bus("TATA", 200,20)
print(f"{bus.color}, {bus.name},{bus.speed},{bus.milage}")
car=Car("Alto", 240,15)
print(f"{car.color}, {car.name},{car.speed},{car.milage}")