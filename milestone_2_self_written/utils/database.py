import json

"""
Concerned with storing and retrieving books from a list.
"""

books = []


def add_book(title, author):
    for b in books:
        if title == b['Title'] and author == b['Author']: #check if the book is already in the list
            print('This book already exists!')
            break
    else:
        books.append({'Title': title, 'Author': author, 'Read': False}) #adds book to the list and creates the 'template' that other functions will run on
        print("Your book has been added!")

def list_books():
    for book in books:
        #print(f"book:{book}")
        print(f"Title: {book['Title']}, Author: {book['Author']}, Read: {book['Read']}") #lists all of the books

def prompt_read_book(book_name):
    for b in books:
        if book_name == b['Title']: #checks if a book is in the list by object name
            b['Read'] = True #changes 'Read' status to True
            print(f"You've read {b['Title']} now!")
            break
    else:
        print("This book doesn\'t exist.")
def prompt_delete_book(book_name):
    for b in books:
        if book_name == b['Title']:  # checks if a book is in the list by object name
            books.remove(b) #deletes the book
            print(f"You've deleted {b['Title']} now!")
            break
    else:
        print("This book doesn\'t exist.")

def save_book_list():
    with open("books_list.json", "w") as booksfile: #save to a file in json format
        book_contents = json.dump(books, booksfile)
        print("Book list saved!")
        return book_contents

def load_book_list():
    with open('books_list.json', 'r') as booksfile: #loads the file in json format
        book_contents = json.load(booksfile)
        for b in book_contents:
            books.append(b)
        print("Book list loaded!")
