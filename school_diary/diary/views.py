from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from urllib.parse import unquote
from .forms import CustomStudentCreationForm
from .models import Students
from django.contrib.auth import authenticate


def index(request):
    if request.method == 'POST':
        form = CustomStudentCreationForm(request.POST)
        if form.is_valid():
            return HttpResponse('da')
        else:
            form = CustomStudentCreationForm()
            return render(request, 'registration.html', {'form': form, 'display': 'block'})
    else:
        form = CustomStudentCreationForm()
        return render(request, 'registration.html', {'form': form, 'display': 'none'})