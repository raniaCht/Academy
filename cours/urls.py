from django.contrib import admin
from django.urls import path
from . import views

app_name = 'cours'

urlpatterns = [
    path('list/', views.cours_list, name='cours_list'),
    path('detail/<int:id>', views.cours_detail, name='cours_detail'),
    path('inscription/<int:id>', views.inscription_cours, name='inscription_cours'),
]