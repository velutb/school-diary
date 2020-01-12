from django.shortcuts import render
from .forms import GetMinimumForm
from django.http import HttpResponse


def minimum(request):
    if request.method == 'POST':
        form = GetMinimumForm(request.POST)
        if form.is_valid():
            chosen_grade = form.cleaned_data['grade']
            chosen_subject = form.cleaned_data['subject']
            chosen_quater = form.cleaned_data['quater']
            filename = str(chosen_subject) + str(chosen_grade) + str(chosen_quater) + ".doc"
            return render(request, 'minimum_download.html', {'filename': filename})
    else:
        form = GetMinimumForm()
    return render(request, 'minimum.html', {'form': form})
