class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
    
    def describe(self):
        print(f"Book Details: '{self.title}' by {self.author}, published in {self.year_published}")

# Creating book objects
book1 = Book("He's into Her", "Maxinejiji", 2013)
book2 = Book("Ang Mutya ng Section E", "Eatmoretobehappy", 2019)
book3 = Book("Mafia Boss", "Khardine Gray", 2019)

# Displaying book details
book1.describe()
book2.describe()
book3.describe()
