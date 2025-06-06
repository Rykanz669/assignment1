class Book:
    def __init__(self, name, stock, id):
        self.id = id
        self.name = name
        self.stock = stock
class Library:
     def __init__(self, books):
        self.books = books
     def issue_book(self, id):
         for book in self.books:
             if book.id == id:
                 book.stock -= 1
     def collect_book(self,id):
         for book in self.books:
             if book.id == id:
                 book.stock += 1
         

 
book_1 = Book("Atomic Structures", 10, 123)
book_2 = Book("Rich dad poor dad", 5, 456)
library = Library([book_1, book_2])
print(library.books[0].stock)
library.issue_book(123)
print(library.books[0].stock)
library.collect_book(123)
print(library.books[0].stock)
 
 