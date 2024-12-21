class Car():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car = Car("Toyota", "Red")
car.brand = "Suzuki"
car.color = "blue"

car1 = Car("Honda", "black")

print(car.brand)
print(car.color)
print(car1.brand)
print(car1.color)
