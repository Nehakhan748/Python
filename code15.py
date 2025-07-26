import json
# import os

def load_books():
    try:
        with open("books.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("No JSON file found.")
        return []
    except json.JSONDecodeError:
        print("File is empty or corrupted.")
        return []

def save_books(books):         #Function to save books:
 with open("books.json", "w") as f:
     json.dump(books , f)

def add_books():
    books = load_books()  # Load existing books:
    while True:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        # Create a dictionary for the book
        book = {"title": title, "author": author}
        books.append(book)  # Add to the list
        count = input("Add another book? (yes/no): ").strip().lower()
        if count != "yes":
            break
    save_books(books)
    print("Books saved successfully!")

def view_books():               #View Function:
    books = load_books()
    if not books:
        print("No books found.")
    else:
        print("----Stored Books----")
        for book in books :
            print(f"-> Title: {book['title']}, Author: {book['author']}")

#Infinite while-loop:
while True:
    print("-----JSON Book Manager-----")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")
#ask user for choice to perform different tasks:
    choice = int(input("Select an option: "))
    if choice == 1:
        add_books()
    elif choice == 2:
        view_books()
    elif choice == 3:
        print("Exit!")
        break
    else:
        print("Invalid choice. Please try again.")