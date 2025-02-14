import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Worldbooks.settings")
django.setup()

from books.models import Book

print("Creating books...")

boos = [
    Book(title="The Catcher in the Rye", author="J.D. Salinger", price=10.00, 
        publisher="Little, Brown and Company", release_date="1951-07-16"),
    Book(title="To Kill a Mockingbird", author="Harper Lee", price=15.00,
        publisher="J.B. Lippincott & Co.", release_date="1960-07-11"),
    Book(title="1984", author="George Orwell", price=12.00,
        publisher="Secker & Warburg", release_date="1949-06-08"),
    Book(title="The Great Gatsby", author="F. Scott Fitzgerald", price=11.00,
        publisher="Charles Scribner's Sons", release_date="1925-04-10"),
    Book(title="Pride and Prejudice", author="Jane Austen", price=14.00,
        publisher="T. Egerton, Whitehall", release_date="1813-01-28"),
    Book(title="The Diary of a Young", author="Anne Frank", price=13.00,
        publisher="Contact Publishing", release_date="1947-06-25"),
    Book(title="The Book Thief", author="Markus Zusak", price=16.00,
        publisher="Picador", release_date="2005-03-14"),
    Book(title="The Hobbit", author="J.R.R. Tolkien", price=17.00,
        publisher="George Allen & Unwin", release_date="1937-09-21"),
    Book(title="The Lord of the Rings", author="J.R.R. Tolkien", price=18.00,
        publisher="George Allen & Unwin", release_date="1954-07-29"),
    Book(title="The Wise Man´s Fear", author="Patrick Rothfuss", price=19.00,
        publisher="DAW Books", release_date="2011-03-01"),
    Book(title="The Name of the Wind", author="Patrick Rothfuss", price=20.00,
        publisher="DAW Books", release_date="2007-03-27"),
    Book(title="The Way of Kings", author="Brandon Sanderson", price=21.00,
        publisher="Tor Books", release_date="2010-08-31"),
    
]

for book in boos:
    book.save()