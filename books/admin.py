from django.contrib import admin

from books.models.book import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'reference', 'edited_date')
    exclude = ('deleted',)

    list_display = ('title', 'author', 'reference')
