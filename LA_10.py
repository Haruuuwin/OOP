class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def describeVehicle(self):
        print(f"{self.brand} is a {self.model} vehicle with a {self.fuel_type} fuel.")

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

suzuki = Car("Suzuki", "Swift", "Petrol")
suzuki.describeVehicle()

raider = Motorcycle("Raider", "R15", "Petrol")
raider.describeVehicle()
