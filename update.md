# 4️⃣ UPDATE the Book
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
Book.objects.get(id=book.id).title
# Expected Output: 'Nineteen Eighty-Four'

