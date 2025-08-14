class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.__price = price
        self.quantity = quantity

    def apply_discount(self, percent):
        self.__price -= self.__price * (percent / 100)

    def restock(self, amount):
        self.quantity += amount

    def get_price(self):
        return self.__price

    def __add__(self, other):
        if self.product_id == other.product_id:
            return Product(self.product_id, self.name, self.__price, self.quantity + other.quantity)
        return NotImplemented

    def __call__(self):
        return f"{self.name} - ${self.__price} ({self.quantity} in stock)"

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, file_size):
        super().__init__(product_id, name, price, quantity)
        self.file_size = file_size

    def apply_discount(self, percent):
        if percent <= 20:
            super().apply_discount(percent)

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, weight):
        super().__init__(product_id, name, price, quantity)
        self.weight = weight

    def apply_discount(self, percent):
        new_price = self.get_price() - (self.get_price() * (percent / 100))
        if new_price >= 5:
            super().apply_discount(percent)

p1 = DigitalProduct(1, "E-Book", 15, 10, "5MB")
p2 = PhysicalProduct(2, "Laptop", 800, 5, "2kg")
p1.apply_discount(15)
p2.apply_discount(50)
print(p1())
print(p2())
p3 = PhysicalProduct(2, "Laptop", 800, 3, "2kg")
p4 = p2 + p3
print(p4())
