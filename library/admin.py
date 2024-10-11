from django.contrib import admin
from library.models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'date_birth', 'date_death')
    list_filter = ('date_birth', 'date_death')
    search_fields = ('last_name', 'first_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'genre', 'status')
    list_filter = ('author', 'genre', 'status')
    search_fields = ('name',)
