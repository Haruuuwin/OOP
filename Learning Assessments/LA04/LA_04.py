class mobaylhero():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name} is a/an {self.role} hero."
        
fighter = mobaylhero("Balmond", "fighter")
assassin = mobaylhero("Saber", "assassin")

print(fighter.name)
print(fighter.role)
print(fighter)
print(assassin.name)
print(assassin.role)
print(assassin)
