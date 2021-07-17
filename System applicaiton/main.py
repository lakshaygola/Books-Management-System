''' Book Store management '''

import Functions as funcs
import os
from book import Book

# Function to take the input from the user
funcs.printOptions()
option = int(input())

# books list - store all the books information in the form of dictornary
booksList = []

while option != 0:

    if (option == 1):
        booksList.append(funcs.createBook())
        input('Book is created... Press Enter continue')
        print(booksList)

    elif (option == 2):
        flag = funcs.saveBook(booksList)
        if(flag):
            input('Book is saved locally... Press Enter to continue')
        else:
            input('Books are not saved in the disk')

    elif (option == 3):
        loadedBooks = funcs.loadBook()
        print(loadedBooks)
        if (loadedBooks):
            input('Book loaded in your drive...press Enter to continue')
        else:
            input('Books are not able to loaded in your drive please try again... Press Enter')

    elif option == 4:
        loadedBooks = funcs.loadBook()
        key = int(input('Enter the ID of book: '))
        idx = funcs.find_book(loadedBooks, key)
        if (idx == None):
            print('This book is not found in the library')
        else:
            print('Book is present in', idx+1, 'shelf')
        input('Press Enter to continue')

    elif option == 5:
        loadedBooks = funcs.loadBook()
        name = funcs.bookIssued(loadedBooks)
        if (name == None):
            print('Book is out of stock')
        else:
            print(f'Book {name} is successfully issued to the user')
        input('Press Enter to continue')

    elif option == 6:
        loadedBooks = funcs.loadBook()
        name = funcs.returnedBook(loadedBooks)
        if name == None:
            print('You must enter the wrong ID please check')
        else:
            print(f'{name} is successfully return to the library')
        input('Press Enter to continue')

    elif option == 7:
        loadedBooks = funcs.loadBook()
        funcs.updateBooks(loadedBooks)
        input("pres Enter to continue")

    elif option  == 8:
        loadedBooks = funcs.loadBook()
        funcs.showAll(loadedBooks)
        input('Press Enter to continue')

    elif option == 9:
        funcs.showSpecific()
        input('Press Enter to continue')

    else:
        print('Please enter the command according to the given menu')

    os.system("cls")
    funcs.printOptions()
    option = int(input())





