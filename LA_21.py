class Pizza:
    def __init__(self, dough, cheese, pineapple, mushroom, pepperoni, tomato_sauce):
        self.__dough = dough
        self.__cheese = cheese
        self._pineapple = pineapple
        self.__mushroom = mushroom
        self.__pepperoni = pepperoni
        self.__tomato_sauce = tomato_sauce

    def __str__(self):
        return f'''My favorite food is Pizza, it has {self.__dough}, {self.__cheese}, {self._pineapple}, {self.__mushroom}, {self.__pepperoni}, {self.__tomato_sauce}.'''
       
    def may_dough_ba(self):
        return self.__dough
       
    def i_set_to(self, bago):
        self.__dough = bago

Hawaiian = Pizza("dough", "mozarella", "pineapple", "mushroom", "pepperoni", "tomato_sauce")
Hawaiian.i_set_to("May dough")
print(Hawaiian.may_dough_ba())
