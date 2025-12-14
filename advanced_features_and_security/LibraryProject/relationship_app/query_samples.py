import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Query all books by a specific author ---
author_name = "J.K. Rowling"  # Replace with any author name you have in your DB
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by author: {books_by_author}")

# --- List all books in a library ---
library_name = "Central Library"  # Replace with your library name
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in library: {books_in_library}")

# --- Retrieve the librarian for a library ---
librarian = Librarian.objects.get(library=library)
print(f"Librarian for the library: {librarian}")
