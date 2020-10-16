from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('inscription', views.inscription, name='inscription'),
    path('profile/', views.profile, name='profil'),
    path('profil/edit', views.profil_edit, name='profil_edit'),
    path('profil/mes-cours', views.mes_cours, name='mes_cours'),
    path('profil/mes-formations', views.mes_formations, name='mes_formations'),
    path('profil/mes-evenements', views.mes_evenements, name='mes_evenements'),
    path('profil/mon-avis', views.mon_avis, name='mon_avis'),
    #path('count-etudiant', views.nbrEtudiant, name='count_etudiant'),
]