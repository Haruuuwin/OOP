from abc import ABC, abstractmethod
class GameChar(ABC):
    @abstractmethod
    def attack(self):
        pass

class Warrior(GameChar):
    def attack(self):
        print("Warrior: Swing sword!")

class Mage(GameChar):
    def attack(self):
        print("Mage: Casts a fireball!")
       
class Archer(GameChar):
    def attack(self):
        print("Archer: Shoots an arrow!")

class Healer(GameChar):
    def attack(self):
        print("Healer: Casts healing spell on ally!")
       
w1 = Warrior()
m1 = Mage()
a1 = Archer()
h1 = Healer()

w1.attack()
m1.attack()
a1.attack()
h1.attack()
