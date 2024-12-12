class AnimeChar:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
       
    def introduce(self, func):
        def name_char(*args, **kwargs):
            print("Introducing...")
            func(*args, **kwargs)
            print("This character is amazing!")
        return name_char
       
uzumaki = AnimeChar("Naruto", "Rasengan")

@uzumaki.introduce

def char_intro(name, ability):
    print(f"I am {name} and I can use {ability}.")
char_intro("Anya", "Telepathy")
