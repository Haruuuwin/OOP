class Car():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self):
        return f"My car, {self.brand}, is color {self.color}"

my_car = Car("Suzuki", "Red")
print(my_car)

del my_car
print(my_car)
