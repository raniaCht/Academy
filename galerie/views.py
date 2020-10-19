from django.shortcuts import render
from .models import Galerie_Formation, Galerie_Evenement
from .filters import GalerieFormationFilter, GalerieEvenementFilter

def formation(request):
    images = Galerie_Formation.objects.all()
    myfilter = GalerieFormationFilter(request.GET,queryset=images)
    images = myfilter.qs
    context = {
        'images' : images,
        'myfilter' : myfilter
    }
    return render(request, 'galerie.html', context)


def evenement(request):
    images = Galerie_Evenement.objects.all()
    myfilter = GalerieEvenementFilter(request.GET,queryset=images)
    images = myfilter.qs
    context = {
        'images' : images,
        'myfilter' : myfilter
    }
    return render(request, 'galerie.html', context)