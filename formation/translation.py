from modeltranslation.translator import translator, TranslationOptions
from .models import Categorie, Formation

class CategorieTranslationOptions(TranslationOptions):
    fields = ('nom', )

translator.register(Categorie, CategorieTranslationOptions)


class FormationTranslationOptions(TranslationOptions):
    fields = ('nom', 'description',)

translator.register(Formation, FormationTranslationOptions)