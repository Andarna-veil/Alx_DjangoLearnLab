# 1️⃣ Import the Book model
from bookshelf.models import Book

# 2️⃣ CREATE a Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected Output: <Book: Book object (1)>

