class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Added '{title}' to {self.name}.")

    def borrow(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"You borrowed '{book.title}'.")
                return
        print(f"'{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"You returned '{book.title}'.")
                return
        print(f"No record of '{title}' being borrowed.")

    def show_books(self):
        for book in self.books:
            print(book)

if __name__ == "__main__":
    library = Library("City Library")
    library.add_book("1984", "George Orwell")
    library.add_book("The Hobbit", "J.R.R. Tolkien")
    library.show_books()
    library.borrow("1984")
    library.show_books()
    library.return_book("1984")
    library.show_books()
