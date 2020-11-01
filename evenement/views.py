from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Evenement, Inscrit_evenement
from accounts.models import Etudiant
from django.utils.translation import gettext as _ 

def evenement_list(request):
    evenement_list = Evenement.objects.all()
    context = {
        'evenements' : evenement_list,
    }
    return render(request, 'evenement_list.html', context)


def evenement_detail(request, id):
    evenement = Evenement.objects.get(id=id)
    context = {
        'evenement' : evenement
    }
    return render(request, 'evenement_detail.html', context)


@login_required
def inscription_evenement(request, id):
    evenement = Evenement.objects.get(id=id)
    etudiant = Etudiant.objects.get(compte=request.user)
    test = Inscrit_evenement.objects.filter(etudiant=etudiant, evenement=evenement)
    if(len(test) == 0):
        inscrit_evenement = Inscrit_evenement(etudiant=etudiant, evenement=evenement)
        inscrit_evenement.save()
        context = {
            'evenement' : evenement
        }
        return redirect(reverse('accounts:mes_evenements'))
    else:
        evenement_list = Evenement.objects.all()
        context = {
            'evenements' : evenement_list,
            'evenement_erreur' : _('Vous être déjà inscrit à cet événement')
        }
        return render(request, 'evenement_list.html', context)