from django.contrib import admin
from django.urls import path
from . import views

app_name = 'formation'

urlpatterns = [
    #path('profil/', views.profil, name='profil'),
    path('list/', views.formation_list, name='formation_list'),
    path('detail/<int:id>', views.formation_detail, name='formation_detail'),
    path('inscription/<int:id>', views.inscription_formation, name='inscription_formation'),
]


