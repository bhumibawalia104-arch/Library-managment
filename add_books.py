from utils import books

def add():
    book_name = input("Enter book name: ").upper()

    if book_name in books:
        print("⚠ Book already exists...")
    else:
        books[book_name] = {"available": True}
        print(f" Book '{book_name}' added successfully")
    
