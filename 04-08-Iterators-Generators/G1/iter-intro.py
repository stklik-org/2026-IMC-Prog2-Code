import random

# for c in "happy birthday":
#     print(c)


it = iter("happy birthday")
# print("The string iterator", it)
#
# nex = next(it)
# print(nex)
#
# print(next(it))
# print(next(it))
# print(next(it))


class RangeIterator():
    def __init__(self, start, stop, step):
        self.n = start
        self.stop = stop
        self.step = step

    def __next__(self):
        self. n += self.step
        if self.n >=self.stop:
            raise StopIteration
        return self.n

class Range():
    def __init__(self, start, stop, step):
        self.n = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return RangeIterator(self.n, self.stop, self.step)


# for c in Range(0,30,3):
#     print (c)


# Rough translation of what a for loop does in Python:

# loop_condition = Range(0, 30, 3)
# rangeIterator = iter(loop_condition)
# try:
#     while True:
#         c = next(rangeIterator)
#         print(c)  # << this is the loop body
#
# except StopIteration:
#     pass

students = ["Tom", "Susy", "Lisa", "Mark", "Stefan"]

itPres = iter(students)
itCleaning = iter(students)

# sc = next(itCleaning)
# print("Next Cleaning = ", sc)
#
# sc = next(itCleaning)
# print("Next Cleaning = ", sc)
#
# sp = next(itPres)
# print("Next Presentation = ", sc)
#
# sc = next(itCleaning)
# print("Next Cleaning = ", sc)


class FibSequence():
    def __init__(self, end):
        self.n = end
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        # Compute which number to return
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

# for c in FibSequence(10):
#     print(c)

class Book():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Library():
    def __init__(self):
        self.__books = []

    def __iter__(self):
        # iter_values = [(id(next_book), str(next_book), next_book)
        #                for next_book in self.__books]
        # return iter(iter_values)
        return BookIterator(self.__books)
    def addBook(self, book):
        self.__books.append(book)


class BookIterator():
    def __init__(self, all_books):
        self.n = 0
        self.books = all_books

    def __next__(self):
        if self.n >= len(self.books):
            raise StopIteration

        next_book = self.books[self.n]
        self.n += 1
        return (id(next_book), next_book.name, next_book)


library = Library()
library.addBook(Book("Huckleberry Finn"))
library.addBook(Book("Tom Sawyer"))
library.addBook(Book("Animal Farm"))
library.addBook(Book("Lord of the flies"))

# for book in library:
#     print(book)


def fibonacci(startA=0, startB=1):
    a = startA
    b = startB
    while True:
        x = a
        a = b
        b = b + x
        yield x

fibo = fibonacci(17, 523)
print("fibo1", next(fibo))
print("fibo1", next(fibo))



fibo2 = fibonacci(0, 1)
for i in range(5):
    print("Fibo2", next(fibo2))

print("fibo1", next(fibo))
print("fibo1", next(fibo))
#


def gen1():
   for char in "Python":
        yield char
   for i in range(5):
        yield i

for v in gen1():
    print(v)

def gen2():
    yield from "Python"
    yield from range(5)

for v in gen2():
    print(v)

def squares():
    i = 0
    while i < 1000:
        yield i * i
        i += 1

sqit = squares()
print(sum(sqit))


# all_values = (random.random() for _ in range(1000))
# min(all_values)







