from modeltranslation.translator import translator, TranslationOptions
from .models import Cours, Matiere


class CoursTranslationOptions(TranslationOptions):
    fields = ('description',)

translator.register(Cours, CoursTranslationOptions)

class MatiereTranslationOptions(TranslationOptions):
    fields = ('nom', )

translator.register(Matiere, MatiereTranslationOptions)