from bookshelf.models import Book

# Retrieve the book we created
book = Book.objects.get(id=1)
book  # Expected output: <Book: 1984>
