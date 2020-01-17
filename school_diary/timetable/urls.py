from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetable, name='timetable'),
    path('get', views.get, name='timetable_get'),
    path('download/', views.download, name='timetable_download'),
]
