class Library:
    def __init__(self):
        self.noBook = 0
        self.book = []

    @property
    def Book(self):
        print(self.book)

    @Book.setter
    def Book(self,name):
        self.book.append(name)
        self.noBook += 1
    
    def check(self):
        if(self.noBook == len(self.book)):
            print(f"The program is correct and no of books {self.noBook}")

        else:
            print("Error in the program")

lib = Library()
lib.Book='Bhagwat Gita'
lib.Book='A brief History of Time'
lib.Book='Rich Dad Poor Dad'
lib.Book='Sapiens'
lib.Book='Atomic habits'
lib.Book='Phychology of Money'
lib.Book='Ikigai'
lib.Book='How to win friend and Influence People'
lib.Book='Harry Potter'

lib.Book
lib.check()
