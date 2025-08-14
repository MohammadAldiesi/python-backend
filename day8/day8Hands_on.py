class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        return f"{self.brand} is moving"

class Car(Vehicle):
    def move(self):
        return f"{self.brand} car is driving"

class Bike(Vehicle):
    def move(self):
        return f"{self.brand} bike is riding"

vehicles = [Car("Mercedes"), Bike("Ducatti")]
for v in vehicles:
    print(v.move())
