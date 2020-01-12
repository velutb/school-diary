from django.shortcuts import render
from .forms import GetMinimumForm

def minimum(request):
    if request.method == 'POST':
        form = GetMinimumForm(request.POST)
        if form.is_valid():
            chosen_grade = form.cleaned_data['grade']
            chosen_subject = form.cleaned_data['subject']
            chsoen_quater = form.changed_data['quater']
            filename = str(chosen_subject) + str(chosen_grade) + str(chsoen_quater)
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
    else:
        form = GetMinimumForm()
    return render(request, 'minimum.html', {'form': form})


def minimum_download(request):
    return render(request, 'minimum_download.html')
