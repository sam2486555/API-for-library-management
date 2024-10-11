from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from library.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')


class AuthorRetrieveSerializer(serializers.ModelSerializer):
    books = SerializerMethodField()

    def get_books(self, author):
        queryset = [book.name for book in Book.objects.filter(author=author.pk)]
        return queryset

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'genre', 'status')


class BookRetrieveSerializer(serializers.ModelSerializer):
    owner = SerializerMethodField()

    def get_owner(self, book):
        if book.owner:
            owner = [book.owner.email for book in Book.objects.filter(owner=book.owner.pk)]
            if owner:
                return ''.join(owner)
            return None

    class Meta:
        model = Book
        fields = '__all__'
