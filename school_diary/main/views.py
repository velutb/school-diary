from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html')


def social(request):
    return render(request, 'social.html')
