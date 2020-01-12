from django.urls import path
from . import views


urlpatterns = [
    path('', views.minimum, name='minimum'),
    path('list/', views.minimum_download, name='minimum_download'),
]
