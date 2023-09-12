class Library:
    def available_books(self, books, author):
        print()
        for i in range(len(books)):
            print(f"Book: {books[i]}")
            print(f"Author: {author[i]}")
            print()

    def issue_book(self, book, author, lis1, name1):
        Students = ["Ranjit", "Elon", "Steve", "Dynamo"]
        student = []
        for i in Students:
            student.append(i.lower())

        while True:
            Name = str(input("Enter your name:-"))
            name = Name.lower()

            if name not in student:
                print("You are not a student of our library\n")
            else:
                book_name = int(input("Enter book no:-"))
                a = book.pop(book_name-1)
                author.pop(book_name-1)
                lis1.append(a)
                name1.append(name)
                print("The book", a, "has been issued to", name, "\n")
                break
        return lis1, name1

    def add_book(self, book, author):
        new_book = str(input("Enter book name:-"))
        new_author = str(input("Enter author name:-"))
        if new_book not in book:
            book.append(new_book)
            author.append(new_author)
            print("The book", new_book, "has been added to the library\n")
        else:
            print("The book", new_book, "is already in the library\n")

    def return_books(self, book, author, issued_book, issued_t):
        Name = str(input("Enter your name:-"))
        student_name = Name.lower()
        if student_name not in issued_t:
            print("We have not issued any book to you\n")
        else:
            book_name = str(input("Enter book name:-"))
            author_name = str(input("Enter author name:-"))
            if book_name not in issued_book:
                print("We have not issued this book!\n")
            else:
                for i in range(len(issued_book)):
                    if issued_book[i] == book_name and issued_t[i] == student_name:
                        book.append(book_name)
                        author.append(author_name)
                        print("The book", book_name, "has been returned by", student_name, "\n")
                        break
                    else:
                        print("The book has not been returned")


books = ["Rich dad poor dad", "The science of getting rich", "Power of our subconscious mind",
         "Structures or why things don't fall down", "The hitchhikers guide to the galaxy"]
authors = ["Robert Kiosaki", "Wallace Wattles", "Joseph Murphy", "J.E Gordon", "Douglas Adams"]

lb = Library()
list1 = []
names = []
while True:
    print("1 --> Show available books\n2 --> Issue books\n3 --> Add book\n4 --> Return issued books\n5 --> Exit")
    choice = int(input("Enter your choice:-"))
    if choice == 1:
        lb.available_books(books, authors)
    elif choice == 2:
        issued_books, issued_to = lb.issue_book(books, authors, list1, names)
    elif choice == 3:
        lb.add_book(books, authors)
    elif choice == 4:
        lb.return_books(books, authors, issued_books, issued_to)
    else:
        break

"""
    Create a library management system which is capable of issuing books to the students.
    Books should information like:-
    1. Book name
    2. Author name
    3. Issued to
    4. Issued on
    User should be able to add books, return issued books, issue books
    Assume that all the users are registered with their names in the central database
"""
