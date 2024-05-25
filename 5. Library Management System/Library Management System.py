class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def display_available_books(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("- " + book)

    def borrow_books(self, bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            print(
                f"\nYou have been issued {bookName}. Keep it safe & Return in 30 Days."
            )
            return True
        else:
            print(
                "\nSorry! This book is already issued. Wait until the book is returned."
            )
            return False

    def return_book(self, bookName):
        self.books.append(bookName)
        print(
            "\nThanks for returning the book on time! Hope you enjoyed reading. Have a nice day!"
        )


class Student:
    def request_book(self):
        self.book = input("\nEnter the book you want to issue: ")
        return self.book

    def return_book(self):
        self.book = input("\nEnter the book you want to return: ")
        return self.book


if __name__ == "__main__":
    TheGreatLibrary = Library(
        [
            "Think and Grow Rich",
            "Cant Hurt Me",
            "Atomic Habits",
            "48 Laws Of Power",
        ]
    )
    Student = Student()

    while True:
        welcomemsg = """
        ╔══════════════════════════════════════════════════╗
        ║            Welcome To Abby's Library             ║
        ║  The place where you can get your desired book   ║
        ╚══════════════════════════════════════════════════╝

        Please Choose an Option:

        1. List of all the books.
        2. Request a book.
        3. Return a book.
        4. Exit

        """
        print(welcomemsg)
        a = int(input("Enter the option number: "))

        if a == 1:
            TheGreatLibrary.display_available_books()
        elif a == 2:
            TheGreatLibrary.borrow_books(Student.request_book())
        elif a == 3:
            TheGreatLibrary.return_book(Student.return_book())
        elif a == 4:
            print("Thanks for choosing The ADZIZ's Library! Have a great day ahead.")
            break
        else:
            print("Invalid Option!")
