from .models import Galerie_Formation, Galerie_Evenement
import django_filters

class GalerieFormationFilter(django_filters.FilterSet):
    class Meta:
        model = Galerie_Formation
        fields = ['formation',]

class GalerieEvenementFilter(django_filters.FilterSet):
    class Meta:
        model = Galerie_Evenement
        fields = ['evenement',]