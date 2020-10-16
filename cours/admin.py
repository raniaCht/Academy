from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Annee, Cours, Matiere, Niveau_scolaire

class CoursAdmin(TranslationAdmin):
    model = Cours
    list_display = ('id', 'matiere', 'niveau', 'annee')
    search_fields = ['matiere', 'matiere', 'niveau', 'annee']
    list_filter = ('matiere',)

admin.site.register(Cours, CoursAdmin)


class MatiereAdmin(TranslationAdmin):
    model = Matiere
    list_display = ('id', 'nom',)
    search_fields = ['nom',]
    list_filter = ('nom',)

admin.site.register(Matiere, MatiereAdmin)

class AnneeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom',)
    search_fields = ['nom',]
    list_filter = ('nom',)

admin.site.register(Annee, AnneeAdmin)


class Niveau_scolaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom',)
    search_fields = ['nom',]
    list_filter = ('nom',)

admin.site.register(Niveau_scolaire, Niveau_scolaireAdmin)




