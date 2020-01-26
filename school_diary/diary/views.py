from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from urllib.parse import unquote
from .forms import StudentRegistration
from django.contrib.auth import authenticate


def index(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            user = authenticate()
            return HttpResponse('True')
    else:
        form = StudentRegistration()
        return render(request, 'registration.html', {'form':form})