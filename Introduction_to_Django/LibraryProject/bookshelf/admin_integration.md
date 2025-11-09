# Django Admin Integration for Book Model

## 1. Register the Book Model
In `bookshelf/admin.py`, we imported the Book model and registered it with the admin:

```python
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)
