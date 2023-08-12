class Library:
    def __init__(self, par_books_list):
        self.books_list = par_books_list
        self.lend_book_dict = {}  # This dictionary shows the books who is already being used by someone(borrower name)

    def display_books(self):
        print("\nWe have the following books available in our Library:-")
        for item in self.books_list:
            print(item)

    def lend_book(self, par_book_name):

        if par_book_name not in self.lend_book_dict.keys():
            borrower_name = input("Enter your name : ")
            print("\nWait a second! We are updating our database...")
            self.lend_book_dict.update({par_book_name: borrower_name})
            import time
            time.sleep(1)
            print("\nLibrary database has been updated.\nYou can take the book now.\nThank You!")

        else:
            print(f"This book is already using by {self.lend_book_dict.get(par_book_name)}.")

    def add_book(self, par_add_book_name):
        var_add_book_name = par_add_book_name

        print("\nWait a second! Database is updating...")
        self.books_list.append(par_add_book_name)
        import time
        time.sleep(1)
        print(f"\nBook named '{var_add_book_name}' is added now in the Library database.\nThank You!")

    def return_book(self, par_return_book_name):
        var_return_book_name = par_return_book_name

        returner_name = input("Enter your name : ").split(" ")[0]

        print("\nWait a second! We are updating our database...")
        self.lend_book_dict.pop(var_return_book_name)
        import time
        time.sleep(1)
        print(f"\nHey {returner_name}!\nYou have successfully returned the book named '{var_return_book_name}' is now added back in our Library database.\nThank You!")


if __name__ == '__main__':

    list_of_available_books = Library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'])

    print("\n------------WELCOME TO OUR LIBRARY------------")

    while True:
        print("\nHi, What do you want? \n1) Display books \n2) Lend a book \n3) Add a book \n4) Return a book \n5) Exit")
        inp1 = input("\nEnter your choice : ")

        if inp1 == "1":
            list_of_available_books.display_books()

        elif inp1 == "2":
            book_name = input("\nEnter the name of the book you are borrowing : ")
            list_of_available_books.lend_book(book_name)

        elif inp1 == "3":
            add_book_name = input("\nEnter the name of the book you are adding : ")
            list_of_available_books.add_book(add_book_name)

        elif inp1 == "4":
            return_book_name = input("\nEnter the name of the book you are returning : ")
            list_of_available_books.return_book(return_book_name)

        elif inp1 == "5":
            exit()

        else:
            print("\nWrong Input! Please, Enter valid input...", end="\n\n")
            continue


        # HANDLE THE WRONG INPUT AFTER 1st PHASE.
        inp2 = ""
        while inp2 != "c" and inp2 != "e":
            inp2 = input("\nPress 'c' to Continue or 'e' to Exit : ").lower()

            if inp2 == "c":
                continue

            elif inp2 == "e":
                exit()

            else:
                print("\nWrong Input! Please, Enter valid input...")
                continue