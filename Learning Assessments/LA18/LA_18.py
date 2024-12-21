class Pizza:
    def __init__(self, dough, cheese, pineapple, mushroom, pepperoni, tomato_sauce):
        self.__dough = dough
        self.__cheese = cheese
        self.__pineapple = pineapple
        self.__mushroom = mushroom
        self.__pepperoni = pepperoni
        self.__tomato_sauce = tomato_sauce

    def __str__(self):
        return f'''My favorite food is Pizza, it has {self.__dough}, {self.__cheese}, {self.__pineapple}, {self.__mushroom}, {self.__pepperoni}, {self.__tomato_sauce}.'''

Hawaiian = Pizza("dough", "mozarella", "pineapple", "mushroom", "pepperoni", "tomato_sauce")
print(Hawaiian)
