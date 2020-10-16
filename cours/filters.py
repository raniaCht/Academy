import django_filters
from .models import Cours

class CoursFilter(django_filters.FilterSet):
    class Meta:
        model = Cours
        fields = ['niveau', 'annee', 'matiere']