from utils import books, issued_books
import datetime

def calculate_fine(late_days):
    fine = 0
    base = 10

    for i in range(1, late_days + 1):
        week = (i - 1) // 7 + 1
        rate = base

        for j in range(1, week + 1):
            rate *= j

        fine += rate

    return fine


def return_book():
    book_name = input("Enter book name: ").upper()

    if book_name not in issued_books:
        print("Book  not issued")
        return

    record = issued_books[book_name]

    today = datetime.date.today()
    issue_date = record["issue_date"]
    allowed_days = record["days"]

    used_days = (today - issue_date).days

    print(f"\nIssue Date: {issue_date}")
    print(f"Return Date: {today}")
    print(f"Used Days: {used_days}")

    if used_days <= allowed_days:
        print("Returned on time")
    else:
        late = used_days - allowed_days
        fine = calculate_fine(late)

        print(f"⚠ Late by {late} days")
        print(f" Fine: ₹{fine}")

    books[book_name]["available"] = True
    del issued_books[book_name]

    print("Book returned successfully")