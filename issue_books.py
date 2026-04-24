from utils import books, issued_books
import datetime

def issue():
    book_name = input("Enter book name: ").upper()

    if book_name not in books:
        print("Book not found")
        return

    if not books[book_name]["available"]:
        print("Book already issued")
        return

    student = input("Enter student name: ")
    days = int(input("Enter number of days: "))

    issue_date = datetime.date.today()

    issued_books[book_name] = {
        "student": student,
        "issue_date": issue_date,
        "days": days
    }

    books[book_name]["available"] = False

    print(f"\n Book issued to {student}")
    print(f"Issue Date: {issue_date}")
    print(f"Return within {days} days")

    print("\n⚠ Fine Rules:")
    print("1st week → ₹10/day")
    print("2nd week → ₹20/day")
    print("3rd week → ₹60/day")