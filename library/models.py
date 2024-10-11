from django.db import models
from django.utils import timezone
from config.settings import NULLABLE
from users.models import User


class Author(models.Model):
    first_name = models.CharField(
        unique=True,
        max_length=60,
        verbose_name='Имя автора',
        help_text='Укажите имя автора книги'
    )
    last_name = models.CharField(
        unique=True,
        max_length=60,
        verbose_name='Фамилия автора',
        help_text='Укажите фамилию автора книги'
    )
    biography = models.TextField(
        verbose_name='Биография автора',
        help_text='Заполните биографию автора'
    )
    date_birth = models.DateField(
        default=timezone.localdate,
        verbose_name='Дата рождения',
        help_text='Укажите дату рождения автора'
    )
    date_death = models.DateField(
        verbose_name='Дата смерти',
        help_text='Укажите дату смерти автора',
        **NULLABLE
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    GENRE = (
        ('Comedy', 'Комедия'),
        ('Horror', 'Ужасы'),
        ('fantasy', 'Фантастика')
    )
    STATUS = (
        ('Issued', 'Выдана'),
        ('In_stock', 'В наличии')
    )
    name = models.CharField(
        unique=True,
        max_length=60,
        verbose_name='Название книги',
        help_text='Укажите название книги'
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name='Автор книги',
        help_text='Укажите автора книги'
    )
    genre = models.CharField(
        choices=GENRE,
        verbose_name='Жанр книги',
        help_text='Укажите жанр книги',
    )
    status = models.CharField(
        choices=STATUS,
        verbose_name='Статус книги',
        help_text='Укажите статус книги',
        default=STATUS[1][0]
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Пользователь книги',
        help_text='Укажите пользователя книги',
        **NULLABLE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
