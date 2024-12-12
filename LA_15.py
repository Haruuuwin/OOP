class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: Bark!")

class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: Meow")

class Bird:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: Chirp")

class Fish:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: ...")

dog = Dog("Chihuahua")
cat = Cat("Calico")
bird = Bird("Maya")
fish = Fish("Clownfish")

def animal_sounds(animal):
    animal.speak()

animals = [dog, cat, bird, fish]
for animal in animals:
    animal.speak()
