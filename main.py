# main.py

from library import Library, Book

def main():
    library = Library()

    # Add some books
    library.add_book(Book(1, "1984", "George Orwell"))
    library.add_book(Book(2, "To Kill a Mockingbird", "Harper Lee"))

    print("Welcome to the Library System")
    while True:
        print("\nMenu:")
        print("1. Search for a book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            book = library.search_book(title)
            if book:
                print(f"Book found: {book.title} by {book.author}")
            else:
                print("Book not found.")
        elif choice == "2":
            title = input("Enter the book title to borrow: ")
            book = library.search_book(title)
            if book:
                if book.borrow():
                    print(f"You have borrowed '{book.title}'.")
                else:
                    print(f"'{book.title}' is already borrowed.")
            else:
                print("Book not found.")
        elif choice == "3":
            title = input("Enter the book title to return: ")
            book = library.search_book(title)
            if book:
                if book.return_book():
                    print(f"'{book.title}' has been returned.")
                else:
                    print(f"'{book.title}' was not borrowed.")
            else:
                print("Book not found.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
