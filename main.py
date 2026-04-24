from add_books import add
from issued_books import issue
from show_books import show
from return_books import return_book

def library():
    while True:
        print("\n" + "="*40)
        print(" LIBRARY MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
        except:
            print(" Enter valid number")
            continue

        if choice == 1:
            add()
        elif choice == 2:
            show()
        elif choice == 3:
            issue()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank you!")
            break
        else:
            print(" Invalid choice")

library()