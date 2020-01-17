from django.shortcuts import render
from .forms import GetTimeTableForm
from django.http import HttpResponse
from .models import Grades, Lessons 

def timetable(request):
    if request.method == 'POST':
        form = GetTimeTableForm(request.POST)
        if form.is_valid():
            chosen_grade = form.cleaned_data['grade']
            chosen_litera = form.cleaned_data['litera']
            chosen_class = str(chosen_grade) + chosen_litera
            try:
                my_grade = Grades.objects.get(number=chosen_grade, letter=chosen_litera)
                lessons_list_monday = Lessons.objects.filter(connection=my_grade.id, day="Понедельник")
                lessons_list_tuesday = Lessons.objects.filter(connection=my_grade.id, day="Вторник")
                lessons_list_wednesday = Lessons.objects.filter(connection=my_grade.id, day="Среда")
                lessons_list_thursday = Lessons.objects.filter(connection=my_grade.id, day="Четверг")
                lessons_list_friday = Lessons.objects.filter(connection=my_grade.id, day="Пятница")
                lessons_list_saturday = Lessons.objects.filter(connection=my_grade.id, day="Суббота")
                return render(request, 'timetable_list.html', {
                    'my_grade': chosen_class,
                    'monday': lessons_list_monday,
                    'tuesday': lessons_list_tuesday,
                    'wednesday': lessons_list_wednesday,
                    'thursday': lessons_list_thursday,
                    'friday': lessons_list_friday,
                    'saturday': lessons_list_saturday})
            except Exception:
                return render(request, 'error.html', {
                    'error': "404", 
                    'title': "Расписание не найдено", 
                    "description": "Ваш класс отсутствует в базе данных."
                })
    else:
        form = GetTimeTableForm()
    return render(request, 'timetable.html', {'form': form})


def download(request):
    return render(request, 'timetable_download.html')


def get(request):
    chosen_litera = request.GET.get("l",'')
    chosen_grade = request.GET.get("g",0)
    chosen_class = str(chosen_grade) + chosen_litera
    try:
        my_grade = Grades.objects.get(number=chosen_grade, letter=chosen_litera)
        lessons_list_monday = Lessons.objects.filter(connection=my_grade.id, day="Понедельник")
        lessons_list_tuesday = Lessons.objects.filter(connection=my_grade.id, day="Вторник")
        lessons_list_wednesday = Lessons.objects.filter(connection=my_grade.id, day="Среда")
        lessons_list_thursday = Lessons.objects.filter(connection=my_grade.id, day="Четверг")
        lessons_list_friday = Lessons.objects.filter(connection=my_grade.id, day="Пятница")
        lessons_list_saturday = Lessons.objects.filter(connection=my_grade.id, day="Суббота")
        return render(request, 'timetable_list.html', {
            'my_grade': chosen_class,
            'monday': lessons_list_monday,
            'tuesday': lessons_list_tuesday,
            'wednesday': lessons_list_wednesday,
            'thursday': lessons_list_thursday,
            'friday': lessons_list_friday,
            'saturday': lessons_list_saturday})
    except Exception as message:
        return HttpResponse("Ваш класс не найден в базе данных. Ошибка: %s" % message)
