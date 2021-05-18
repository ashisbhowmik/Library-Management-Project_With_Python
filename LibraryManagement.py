class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAalilableBook(self):
        print('Books present in this library are: ')
        for book in self.books:
            print('        *' + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued {bookName} book.\nPlease keep it safe and return it within 15 days")
            self.books.remove(bookName)
            return True
        else:
            print(
                'Sorry!, this book is already issued to someone else. Please wait until the book was given')
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print('Thanks for return this book, Have you enjoyed by reading this book')


class Student:

    def reqestBook(self):
        self.books = input(
            'Enter the name of the book that you want to borrow : ')
        return self.books

    def returnBook(self):
        self.books = input(
            'Enter the name of the book that you want to return : ')
        return self.books


if __name__ == '__main__':
    centralLibrary = Library(['Math', 'Python Notes', 'Algorithm', 'Django'])
    # centralLibrary.displayAalilableBook()
    student = Student()

    while(True):
        welcomeMsg = '''**=== Welcome to Central Library ===**
        Please choose an option:

        1. Show the available book list
        2. Request to borrow a book
        3. Return a book 
        4. Exit to the library

'''
        print(welcomeMsg)

        a = int(input('Please Enter a choice :  '))
        if a == 1:
            centralLibrary.displayAalilableBook()
        elif a == 2:
            centralLibrary.borrowBook(student.reqestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print('thaks for using central library"s book, have a good day!')
            exit()

        else:
            print('    Invalid Choice ,,  ****Please choose from the option')
