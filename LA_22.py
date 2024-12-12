class bdayParty:
    def __init__(self, theme, food):
        self.theme = theme
        self.food = food

    def xms(self):
        print("Birthday Foods: Hotdog, Lumpia,Leche Flan")
        self.__secret_dish()
       
    def __secret_dish(self):
        print(f"Ang theme ay {self.theme}:")
        print(f"=> Ang secret dish ay {self.food}")
       
xmas = bdayParty("Christmas", "Cake")
xmas.xms()
print("----------------------")
hlw = bdayParty("Halloween", "Candle Candy")
hlw.xms()
print("----------------------")
easter = bdayParty("Easter Bunny", "Egg Pie")
easter.xms()
