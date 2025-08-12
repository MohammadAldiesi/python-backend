class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def info(self):
        return f"{self.year} {self.brand} {self.model} - Speed: {self.speed} km/h"

    def accelerate(self, kmh):
        self.speed += kmh
        return f"Accelerated by {kmh} km/h. Now at {self.speed} km/h."

    def brake(self, kmh):
        self.speed = max(0, self.speed - kmh)
        return f"Slowed by {kmh} km/h. Now at {self.speed} km/h."

if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla", 2022)
    print(my_car.info())
    print(my_car.accelerate(30))
    print(my_car.brake(10))
