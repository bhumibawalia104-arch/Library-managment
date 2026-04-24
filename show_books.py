from utils import books

def show():
    print("\n Library Books:")
    print("-" * 30)

    if not books:
        print("No books available...")
        return

    for name, data in books.items():
        status = "Available" if data["available"] else "Issued"
        print(f"{name} → {status}")