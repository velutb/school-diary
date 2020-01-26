from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from urllib.parse import unquote
from .forms import StudentRegistration

def index(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            HttpResponse('True')
    else:
        form = StudentRegistration()
        return render(request,'login.html', {'form':form})