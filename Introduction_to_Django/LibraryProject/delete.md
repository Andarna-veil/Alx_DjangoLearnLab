from bookshelf.models import Book

# Delete the book
book = Book.objects.get(id=1)
book.delete()
Book.objects.all()  # Expected output: <QuerySet []>
