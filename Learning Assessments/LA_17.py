class Player:
    def __init__(self, name, health, atk_power):
        self.name = name
        self.health = health
        self.atk_power = atk_power
   
    def attack(self, target):
        target.health -= self.atk_power
        print(f"{self.name} attacks {target.name}!, {self.name} deals {target.name} damage, {target.name} now has only {target.health}")
        print("-----")

    def heal(self, amount):
        self.health += amount
       
himeko = Player("Himeko", 10000, 3600)
welt = Player("Welt", 9000, 3000)

while himeko.health > 0 and welt.health > 0:
    himeko.attack(welt)
    if welt.health <= 0:
        print("Player: ", himeko.name, ", Health: ", himeko.health)
        print("Player: ", welt.name, ", Health: ", welt.health)
        print(f"{himeko.name} wins!")
        break
   
    welt.attack(himeko)
    if himeko.health <= 0:
        print("Player: ", himeko.name, ", Health: ", himeko.health)
        print("Player: ", welt.name, ", Health: ", welt.health)
        print(f"{welt.name} wins!")
        break
   
welt.heal(2000)
print("----")
print(f"{welt.name} restores his health and now has {welt.health}")
