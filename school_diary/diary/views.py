from django.contrib.auth import authenticate, login
from django.shortcuts import render

from .models import Students, Grades
from .forms import StudentCreationForm, StudentsLogin
from django.http import HttpResponseRedirect, HttpResponse

from django.views.generic import TemplateView


class student_reg(TemplateView):
    def get(self, request):
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            form = StudentCreationForm()
            return render(request, 'registration.html', {'form': form, 'display': 'block'})
    def post(self, request):
        form = StudentCreationForm()
        return render(request, 'registration.html', {'form': form, 'display': 'none'})

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
            user = Students.objects.get(email=form.cleaned_data['email'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('not login')
        else:
            form = StudentsLogin()
            # return render(request, 'login.html', {'form': form, 'display': 'block'})

    else:
        form = StudentsLogin()
        return render(request, 'login.html', {'form': form})

def get_diary(request,l,n, subject):
    grade = Grades.objects.get(letter=l, number=n)
    #for student in grade.objects.students_set.all():
        #student.upd_midmark()
    daylist = ['01.02.2020','02.02.2020','03.02.2020']
    return render(request, 'marklist.html', {'grade': grade})