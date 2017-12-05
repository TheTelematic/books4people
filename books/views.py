# Create your views here.
from django.shortcuts import render


def home(request):
    template = 'books/home.html'

    context = {}

    return render(request, template, context)
