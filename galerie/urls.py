from django.contrib import admin
from django.urls import path

from . import views

app_name = 'galerie'

urlpatterns = [
    path('formation', views.formation, name='formation'),
    path('evenement', views.evenement, name='evenement'),
]