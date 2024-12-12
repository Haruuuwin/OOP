class Animal():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describeAnimal(self):
        print(f'''Animal: {self.name}
Type: {self.type}''')

class Fish(Animal):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.canswim = True

nemo = Fish("nemo", "clownfish")
print(nemo.canswim)
