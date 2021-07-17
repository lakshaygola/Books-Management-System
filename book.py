""" Class which store the book information """

class Book:
    def __init__(self, id, name, description, isbn, page_count, issued, author, year):
        self.id = id
        self.name = name
        self.description = description
        self.isbn = isbn
        self.pageCount = page_count
        self.issued = issued
        self.author = author
        self.year = year

    # To dict method to make the dictionary of the given information
    def to_dict(self):
        bookdict = {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'isbn' : self.isbn,
            'pageCounts' : self.pageCount,
            'issued' : self.issued,
            'author' : self.author,
            'year' : self.year
        }
        return bookdict

if __name__ == "__main__":
    book = Book('7835', 'lakshay gola', 'data science', '5478-895-256', 300, True, 'Ram nath koind', 2017)
    print(book.to_dict())
