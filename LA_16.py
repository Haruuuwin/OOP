class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        print("Operating!")

    def info(self):
        print(f'''Brand: {self.brand}
Model: {self.model}''')

class WashingMachine(Appliance):
    def operate(self):
        print("Washing clothes!")

class Refrigerator(Appliance):
    def operate(self):
        print("Keeping food cold!")

class Microwave(Appliance):
    def operate(self):
        print("Heating food!")

condura = WashingMachine("Condura", "wm1")
midea = Refrigerator("Midea", "r1")
samsung = Microwave("Samsung", "m1")

for items in [condura, midea, samsung]:
    items.operate()
    items.info()
