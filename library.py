class Book:
    def __init__(self, title, auth):
        self.title = title
        self.auth = auth
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"'{self.title}' by {self.auth} [{status}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, auth):
        new_book = Book(title, auth)
        self.books.append(new_book)
        print(f"Book added: {title}")

    def list_books(self):
        if not self.books:
            print("\nThe library is currently empty.")
            return
        print("\n--- Library Catalog ---")
        for index, book in enumerate(self.books, 1):
            print(f"{index}. {book}")
        print("-----------------------")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"Success! You checked out '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                    return
        print("Error: Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.is_available = True
                print(f"Success! You returned '{book.title}'.")
                return
        print("Error: This book does not belong to this library.")


# --- Main Execution Block ---
def main():
    my_library = Library()

    # Pre-populating with some data
    my_library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    my_library.add_book("1984", "George Orwell")
    my_library.add_book("The Hobbit", "J.R.R. Tolkien")

    while True:
        print("\n--- Library Menu ---")
        print("1. View Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Add a New Book")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            my_library.list_books()
        elif choice == "2":
            title = input("Enter the title to borrow: ")
            my_library.borrow_book(title)
        elif choice == "3":
            title = input("Enter the title to return: ")
            my_library.return_book(title)
        elif choice == "4":
            t = input("Enter Title: ")
            a = input("Enter Author: ")
            my_library.add_book(t, a)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid selection, try again.")


if __name__ == "__main__":
    main()