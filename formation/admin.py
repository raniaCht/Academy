from django.contrib import admin
from .models import Categorie, Formation, Niveau
from modeltranslation.admin import TranslationAdmin


admin.site.site_header = 'Future Pioneers Academy'
admin.site.site_title = 'Future Pioneers Academy'

class CategorieAdmin(TranslationAdmin):
    model = Categorie

admin.site.register(Categorie, CategorieAdmin)


class FormationAdmin(TranslationAdmin):
    model = Formation

admin.site.register(Formation, FormationAdmin)

class NiveauAdmin(admin.ModelAdmin):
    list_display = ('niveau',)
    list_display_links = ('niveau',)

admin.site.register(Niveau, NiveauAdmin)
