from django.contrib import admin

# Register your models here.
from timetable.models import Grades, Lessons

@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('connection', 'day', 'subject')
    list_filter = ('connection', 'day', 'subject', 'number')

admin.site.register(Grades)