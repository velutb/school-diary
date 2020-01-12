from django.contrib import admin

# Register your models here.
from timetable.models import Grades, Lessons

admin.site.register(Grades)
admin.site.register(Lessons)