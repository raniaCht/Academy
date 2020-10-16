from django.shortcuts import render
from accounts.models import Commentaire

# Create your views here.


def accueil(request):
    topcommentaires = list(Commentaire.objects.filter(acceptable = True,nbrEtoiles=5))
    if len(topcommentaires) > 4 : 
        topcommentaires = topcommentaires[:4]
    return render(request, 'accueil.html', {'topcommentaires':topcommentaires})

def avis(request):
    commentaires = Commentaire.objects.filter(acceptable = True)
    return render(request, 'avis.html', {'commentaires':commentaires})