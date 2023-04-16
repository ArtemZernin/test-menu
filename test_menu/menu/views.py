from django.shortcuts import render


def index(request):
    return render(request, 'page.html')


def page(request, slug):
    return render(request, 'page.html')
