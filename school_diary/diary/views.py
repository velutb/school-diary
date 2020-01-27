from django.shortcuts import render
from .forms import StudentCreationForm, StudentsLogin
from django.http import HttpResponseRedirect


def students_registration(request):
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            form = StudentCreationForm()
            return render(request, 'registration.html', {'form': form, 'display': 'block'})
    else:
        form = StudentCreationForm()
        return render(request, 'registration.html', {'form': form, 'display': 'none'})


def students_login(request):
    if request.method == 'POST':
        form = StudentsLogin(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            form = StudentCreationForm()
            return render(request, 'login.html', {'form': form, 'display': 'block'})
    else:
        form = StudentCreationForm()
        return render(request, 'login.html', {'form': form,})