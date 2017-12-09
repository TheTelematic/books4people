from django.shortcuts import render


def login(request):
    template = 'accounts/login.html'

    context = {}

    return render(request, template, context)
