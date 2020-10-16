from django.contrib import admin
from django.urls import path
from . import views

app_name = 'evenement'

urlpatterns = [
    #path('profil/', views.profil, name='profil'),
    path('list/', views.evenement_list, name='evenement_list'),
    path('inscription/<int:id>', views.inscription_evenement, name='inscription_evenement'),
]