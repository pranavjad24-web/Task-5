class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print("Book borrowed")
        else:
            print("Book not available")

    def return_book(self):
        self.available = True
        print("Book returned")

b = Book("Python", "Guido")
b.borrow()
b.return_book()
