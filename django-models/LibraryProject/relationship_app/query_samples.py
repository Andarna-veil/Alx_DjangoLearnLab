import os
import sys
import django

# Add the outer LibraryProject folder to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Sample data ---
author, created = Author.objects.get_or_create(name="J.K. Rowling")
book, created = Book.objects.get_or_create(title="Harry Potter and the Sorcerer's Stone", author=author)
library, created = Library.objects.get_or_create(name="Central Library")
if not library.books.filter(pk=book.pk).exists():
    library.books.add(book)
librarian, created = Librarian.objects.get_or_create(name="Alice", library=library)

# --- Queries ---
books_by_author = Book.objects.filter(author=author)
print("Books by author:", books_by_author)

books_in_library = library.books.all()
print("Books in library:", books_in_library)

librarian_for_library = Librarian.objects.get(library=library)
print("Librarian of library:", librarian_for_library)
