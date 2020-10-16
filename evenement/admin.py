from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Evenement

class EvenementAdmin(TranslationAdmin):
    model = Evenement
    list_display = ('id', 'titre', 'lieu', 'formatteur')
    search_fields = ['titre', 'formatteur']

admin.site.register(Evenement, EvenementAdmin)
