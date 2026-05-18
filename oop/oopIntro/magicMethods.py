# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self): # returns string form of an object
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other): # compares if 2 objects are equal to eachother
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):# compares if one object is less than another
        return self.pages < other.pages
    
    def __gt__(self, other):# compares if one object is greater than another
        return self.pages > other.pages
    
    def __add__(self, other):# adds number of pages of one book plus another
        return self.pages + other.pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key): # returns an attribute of an object
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return f"Key '{key}' was not found"
        
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, The Witch, and the Wardrobe", "C.S. Lewis", 172)
book4 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 190)

print(book3)
print(book2 == book4)
print(book2 < book3)
print(book2 > book3)
print(book2 + book3)
print("Rowling" in book2)
print(book3['audio'])