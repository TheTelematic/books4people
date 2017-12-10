# Create your views here.
from django.shortcuts import render

from books.models.book import Book


def home(request):
    template = 'books/home.html'

    context = {}

    return render(request, template, context)


def view_all_books(request):
    template = 'books/books.html'

    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, template, context)
