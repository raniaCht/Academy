import django_filters
from .models import Formation

class FormationFilter(django_filters.FilterSet):
    class Meta:
        model = Formation
        fields = ['formation_type', 'categorie']