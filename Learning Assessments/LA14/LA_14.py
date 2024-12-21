class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describeSpiderman(self):
        print(f"Spiderman Name: {self.name}, Spiderman Age: {self.age}")

class Tobby(Spiderman):
    def __init__(self, name, age, movietitle):
        super().__init__(name, age)
        self.movietitle = movietitle

class Andrew(Spiderman):
    def __init__(self, name, age, movietitle):
        super().__init__(name, age)
        self.movietitle = movietitle

class Tom(Spiderman):
    def __init__(self, name, age, movietitle):
        super().__init__(name, age)
        self.movietitle = movietitle

tobby = Tobby("tobby maguire", 49, "Spiderman 1")
andrew = Andrew("andrew garfield", 41, "The Amazing Spiderman")
tom = Tom("tom holland", 28, "No Way Home")

print("Name:", tobby.name.upper(), "\nMovie Title:", tobby.movietitle)
print("Name:", andrew.name.upper(), "\nMovie Title:", andrew.movietitle)
print("Name:", tom.name.upper(), "\nMovie Title:", tom.movietitle)
