class mobaylhero():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        print(f"{self.name} is a/an {self.role} hero.")

fighter = mobaylhero("Balmond", "fighter")
assassin = mobaylhero("Saber", "assassin")

fighter.describe()
assassin.describe()
