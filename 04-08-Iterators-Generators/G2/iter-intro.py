

mylist = [1, 2, 3, 4, 5, 6]

# for i in mylist:
#     print(i)

listiter = iter(mylist)
# print(listiter)

nextElement = next(listiter)
# print(nextElement)

nextElement = next(listiter)
# print(nextElement)


class RangeInterator():
    def __init__(self, start, stop, step):
        self.n = start
        self.stop = stop
        self.step = step

    def __next__(self):
        self.n += self.step
        if self.n >= self.stop:
            raise StopIteration

        return self.n


class Range():
    def __init__(self, start, stop, step):
        self.n = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        # return RangeInterator(self.n, self.stop, self.step)
        return self

    def __next__(self):
        next_val = self.n
        self.n += self.step
        if self.n > self.stop:
            raise StopIteration

        return next_val

# for c in Range(0, 30, 3):
#     print(c)

rangeit = iter(Range(0, 9, 3))
try:
    while True:
        c = next(rangeit)
        # print(c)  # << this is the loop body
except StopIteration:
    pass

# print(next(rangeit))
# print(next(rangeit))
# print(next(rangeit))
# print(next(rangeit))
# print(next(rangeit))


students = ["Susy", "Lisa", "Stefan", "Tom", "Mark", "Travis"]

cleanIt = iter(students)
presIt = iter(students)


# print("Next Presentaiton", next(presIt))
# print("Next Whiteboard", next(cleanIt))
# print("Next Whiteboard", next(cleanIt))
# print("Next Whiteboard", next(cleanIt))
#
# print("Next Presentaiton", next(presIt))
# print("Next Whiteboard", next(cleanIt))
#
# print("Next Whiteboard", next(cleanIt))


class FibSequence():
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a = 0
        self.b = 1


    def __iter__(self):
        return self

    def __next__(self):
        x = self.a
        self.a = self.b
        self.b = x + self.b

        self.count += 1
        if self.count > self.n:
            raise StopIteration

        return x

# print("Fib 1")
fib = FibSequence(10)
# print(next(fib))
# print(next(fib))
# print(next(fib))

# print("Fib 2")
for c in FibSequence(10):
    # print(c)
    pass

class Book():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class BookIterator():
    def __init__(self, all_books):
        self.books = all_books
        self.idx = 0

    def __next__(self):
        if self.idx >= len(self.books):
            raise StopIteration

        book = self.books[self.idx]
        self.idx += 1
        return book, id(book), str(book)

class Library():
    def __init__(self):
        self.__books = []

    def addBook(self, book):
        self.__books.append(book)

    def __iter__(self):
        return BookIterator(self.__books)
        # return iter(self.__books)


library = Library()
library.addBook(Book("Huckleberry Finn"))
library.addBook(Book("Tom Sawyer"))
library.addBook(Book("Animal Farm"))
library.addBook(Book("Lord of the flies"))

# for book in library:
#     print(book)


def exampleGen():
    print("a")
    print("b")
    print("c")
    yield 1

    print("1")
    print("2")
    print("3")
    yield 2

    print("D")
    print("E")
    print("F")
    yield 3

eg = exampleGen()
print("Yielded Value:", next(eg))

print("Yielded Value:", next(eg))

print("Yielded Value:", next(eg))

# print("Yielded Value:", next(eg))  # << 4th time -> StopIteration Error


def fibonacci():
    a = 0
    b = 1

    while True:
        yield a
        x = a
        a = b
        b = b + x

fibo = fibonacci()
for _ in range(10):
    print(next(fibo))

