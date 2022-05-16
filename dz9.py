from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str

book_1 = ('lgoritms','Bhargava Aditya')
book_2 = ('A bite of Python','Swaroop Chitlur')

print(book_1)
print(book_2)