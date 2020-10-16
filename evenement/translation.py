from modeltranslation.translator import translator, TranslationOptions
from .models import Evenement


class EvenementTranslationOptions(TranslationOptions):
    fields = ('titre', 'lieu', 'formatteur')

translator.register(Evenement, EvenementTranslationOptions)