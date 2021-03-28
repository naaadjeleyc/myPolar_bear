from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_countries', views.all_countries, name='all_countries'),
]
