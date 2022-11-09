class Library:

    def __init__(self, books=None):
        '''Initialise the books'''
        if books:
            self.books = books
        else:
            self.books = []


    def add_book(self, book):
        '''Add a book to library'''
        self.books.append(book)


london = Library(['The surrender experiment'])
london.add_book('Clean Coder')
london.add_book('War and Peace')
print(london.books)

new_york = Library()
new_york.add_book('The Power of Now')
print(new_york.books)
