# Import the Book model
from bookshelf.models import Book

# ===== CREATE =====
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
print("Created Book:", book)

# ===== RETRIEVE =====
all_books = Book.objects.all()
print("Books in DB:", all_books)

# ===== UPDATE =====
book.title = "Nineteen Eighty-Four"
book.save()
print("Updated Book:", book)

# ===== DELETE =====
book.delete()
all_books_after_delete = Book.objects.all()
print("Books after deletion:", all_books_after_delete)
