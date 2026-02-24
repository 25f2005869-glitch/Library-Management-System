books = []

def show_menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")


while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        book_name = input("Enter book name: ")
        books.append(book_name)
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in books:
                print("-", book)

    elif choice == "3":
        search = input("Enter book name to search: ")
        if search in books:
            print("Book found!")
        else:
            print("Book not found.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")