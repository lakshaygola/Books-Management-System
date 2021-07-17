# This file contain all the function which we need in book store / library management system
import pandas as pd

from book import Book
import json

# Function to print out all the available functions
def printOptions():
    print('Press the specific button according to the action')
    print('''1 - Create the new book
2 - Save the book locally
3 - Load the book from the disk
4 - Find the books using id
5 - Issue the book
6 - Return the book
7 - Update the book
8 - Show all the book
9 - Show a specific book
0 - Exit the program''')

# Function to take the input about the book
def inputBookInfo():
    temp = input('Press Y/y - if issued: ')
    return {
        'id' : int(input('Create Id for the book: ')),
        'name' : input('Name of the book: '),
        'description' : input('About the book: '),
        'isbn' : input('Enter the isbn number of the book: '),
        'pageCount' : int(input('Total number of pages in the book: ')),
        'issued' : (temp == 'y' or temp == 'Y'),
        'author' : input('Author name: '),
        'year' : int(input('Year at which book is published: '))
    }

# Function to create the new book in the library
def createBook():
    print("Provide the information to create the book")
    info = inputBookInfo()
    book = Book(info['id'], info['name'], info['description'], info['isbn'],
              info['pageCount'], info['issued'], info['author'], info['year'])

    print(book.to_dict())
    return book

# Function to save the books information into the json file
def saveBook(books):
    flag = 0
    json_book = []
    for b in books:
        json_book.append(b.to_dict())
    try:
        with open('books.dat', 'w') as file:
            file.write(json.dumps(json_book, indent = 4))
    except:
        print('We got some error while storing the books')
        flag = 1
    finally:
        if (flag == 1):
            return False
        else:
            return True

# Function to load the book from the json file
def loadBook():
    try:
        f = open('books.dat', 'r')
        loaded_books = json.loads(f.read())
        bookList = []
        for b in loaded_books:
            newObj = Book(b['id'], b['name'], b['description'], b['isbn'],
                        b['pageCounts'], b['issued'], b['author'], b['year'])
            bookList.append(newObj)
        return bookList
    except Exception as e:
        print(e)

# Helper function for the findbook
def comparison(books, key, pos):
    bookobj = books[pos]
    if (bookobj.id == key):
        return True
    elif (bookobj.id < key):
        return 2
    else:
        return -2

# Function to find the book for the given index (assuming the books are sorted base on their id)
def findBook(books, key):
    lo = 0
    hi = len(books)-1

    while (lo <= hi):
        mid = (lo + hi) / 2

        if comparison(books, key, mid):
            return mid
        elif comparison(books, key, mid) == 2:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# Another find function
def find_book(books, key):
    for index, b in enumerate(books):
        if b.id == key:
            flag = 1
            return index
    return None

# Function to issued the book
def bookIssued(books):
    id = int(input('Enter Id of the book: '))
    idx = find_book(books, id)
    if (idx != None):
        if (books[idx].issued == False):
            books[idx].issued = True
            saveBook(books)
            return books[idx].name
    return None

# Function which update the return of the book
def returnedBook(books):
    id = int(input('Enter Id of the book: '))
    idx = find_book(books, id)
    if (idx != None):
        if (books[idx].issued == True):
            books[idx].issued = False
            saveBook(books)
            return books[idx].name
    return None

# Function to update the info of the book
def updateBooks(books):
    id = int(input('Enter ID: '))
    idx = find_book(books, id)
    if id != None:
        new_book = createBook()
        old_book = books[idx]
        books[idx] = new_book
        del old_book
        saveBook(books)
        print('Book is successfully updated')
    else:
        print('You may enter the wrong key')

# Function to print all the books which exist in the dataframe
def showAll(books):
    df = pd.DataFrame()
    for b in books:
        df = df.append(b.to_dict(), ignore_index= True)
    df.to_csv('BookManagement.csv')

# Function to print the specific book
def showSpecific():
    key = int(input('Enter the key: '))
    df = pd.read_csv('BookManagement.csv')
    book = df[df.id == key]
    print(book['name'])





if __name__ == '__main__':
    printOptions()
    bookobj = loadBook()
    print(bookobj)
