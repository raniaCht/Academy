from django.contrib import admin
from django.urls import path

from . import views

app_name = 'accueil'

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('nos-temoignages', views.avis, name='avis'),
    path('about-us', views.about, name='about'),
    #path('count-commentaires', views.nbrCommentaires, name='count_commentaires'),
]