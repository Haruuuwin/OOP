class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("FBBAM", "Yana")
book2 = Book("MHIAMB", "Aimee")

print(book1.title)
print(book1.author)
del book1.author
print(book1.author)
print(book2.title)
print(book2.author)
