from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('differentSignPage/', views.differentSigns, name='differentSigns'),
]