from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 's' to save the book list
- 'lo' to load the saved book list
- 'q' to quit

Your choice:"""

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        pass
        if user_input == 'a':
            title = input('What is the title of your book?').title()
            author = input('Who is the author of your book?').title()
            database.add_book(title, author)
        elif user_input == 'l':
            database.list_books()
        elif user_input == 'r':
            book_name = input('What is the name of your book?').title()
            database.prompt_read_book(book_name)
        elif user_input == 'd':
            book_name = input('What is the name of your book you want to delete?').title()
            database.prompt_delete_book(book_name)
        elif user_input == 's':
            database.save_book_list()
        elif user_input == 'lo':
            database.load_book_list()
        else:
            print('Unknown command. Please try again.')
            pass
        user_input = input(USER_CHOICE)


menu()


