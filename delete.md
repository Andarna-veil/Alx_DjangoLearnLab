# 5️⃣ DELETE the Book
book.delete()
# Expected Output: (1, {'bookshelf.Book': 1})

# Verify deletion
Book.objects.all()
# Expected Output: <QuerySet []>

