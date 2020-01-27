from django.shortcuts import render
from .forms import CustomStudentCreationForm
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        form = CustomStudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')  # TODO Доделать ридерект на главную страницу
        else:
            form = CustomStudentCreationForm()
            return render(request, 'registration.html', {'form': form, 'display': 'block'})
    else:
        form = CustomStudentCreationForm()
        return render(request, 'registration.html', {'form': form, 'display': 'none'})