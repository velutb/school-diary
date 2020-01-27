from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from urllib.parse import unquote
from .forms import StudentRegistration
from .models import Students
from django.contrib.auth import authenticate


def index(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
           try:
               # user = Students.
                return HttpResponse(form.cleaned_data['email'])
           except:
               pass
    else:
        form = StudentRegistration()
        return render(request, 'registration.html', {'form':form})