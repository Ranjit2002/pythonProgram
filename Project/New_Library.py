"""
Write a library class with no_of_books and books as two instance variables. Write a program to create a library
from this Library class and show how you can print all books, add a book and get the number of books using different
methods. Show that your program doesn't persist the books after the program is stopped!
"""

class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = list()

    def add_book(self):
        while True:
            try:
                book_name = str(input("Enter book name:- "))
                self.books.append(book_name)
                self.no_of_books += 1
                break
            except Exception as ex:
                print(type(ex))
                print(ex, "\n")
                continue

    def show_available_books(self):
        if not self.books:
            print("\nNo books are there in the library\n")
        else:
            print()
            for i in range(len(self.books)):
                print(f"{i+1}. {self.books[i]}")
            print()

    def check_len_book_no_of_book(self):
        if self.no_of_books == len(self.books):
            print("\nNumber of books are equal to len of books\n")
        else:
            print("\nNumber of books and len of books are different\n")

    def get_no_of_books(self):
        print(f"\nNumber of books in the library is {self.no_of_books}\n")


a = Library()
while True:
    try:
        print("1 --> Show available books\n2 --> Add book\n3 --> Check len of book is equals to no_of_books\n"
              "4 --> Get number of books\n5 --> Exit")
        choice = int(input("Enter your choice:- "))
        if choice == 1:
            a.show_available_books()
        elif choice == 2:
            a.add_book()
            print()
        elif choice == 3:
            a.check_len_book_no_of_book()
        elif choice == 4:
            a.get_no_of_books()
        elif choice == 5:
            break
        else:
            print("Please enter number between 1 to 5")
            continue
    except Exception as ex:
        print(type(ex))
        print(ex)
