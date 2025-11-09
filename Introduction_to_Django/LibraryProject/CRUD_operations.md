# Django CRUD Operations

## Create
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # Expected output: <Book: 1984>

## Retrieve
Book.objects.all()  # Expected output: <QuerySet [<Book: 1984>]>

## Update
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(id=book.id)  # Expected output: <Book: Nineteen Eighty-Four>

## Delete
book.delete()
Book.objects.all()  # Expected output: <QuerySet []>
