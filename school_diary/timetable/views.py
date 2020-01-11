from django.shortcuts import render


def timetable(request):
    return render(request, 'timetable.html')


def download(request):
    return render(request, 'timetable_download.html')