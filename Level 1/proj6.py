class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

    def borrow(self):
        if self.status == "Available":
            self.status = "Borrowed"
            return True
        else:
            print(f"Sorry, the book '{self.title}' is already borrowed.")
            return False

    def return_book(self):
        if self.status == "Borrowed":
            self.status = "Available"
            return True
        else:
            print(f"The book '{self.title}' was not borrowed.")
            return False

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Status: {self.status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book added: {book.title} by {book.author}")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\nAvailable Books:")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

    def borrow_book(self, book_index):
        if 0 <= book_index < len(self.books):
            book = self.books[book_index]
            if book.borrow():
                print(f"Book borrowed: {book.title}")
        else:
            print("Invalid book selection.")

    def return_book(self, book_index):
        if 0 <= book_index < len(self.books):
            book = self.books[book_index]
            if book.return_book():
                print(f"Book returned: {book.title}")
        else:
            print("Invalid book selection.")


def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            library.add_book(title, author)
        elif choice == 2:
            library.display_books()
        elif choice == 3:
            library.display_books()
            try:
                book_index = int(input("Enter the number of the book to borrow: ")) - 1
                library.borrow_book(book_index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == 4:
            library.display_books()
            try:
                book_index = int(input("Enter the number of the book to return: ")) - 1
                library.return_book(book_index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == 5:
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
