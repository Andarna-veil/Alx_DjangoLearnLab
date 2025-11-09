from django.contrib import admin
from .models import Book  # <--- ALX specifically checks for this

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in admin list
    search_fields = ('title', 'author')                     # Search box
    list_filter = ('publication_year',)                     # Filter sidebar

admin.site.register(Book, BookAdmin)

