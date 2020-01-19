from django.urls import path
from . import views


urlpatterns = [
    path('<int:page>', views.get_posts),
    path('', views.redirect),
    path('articles/<slug:url>', views.post)
]
