from bookshelf.models import Book

# Update the title
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(id=book.id)  # Expected output: <Book: Nineteen Eighty-Four>

