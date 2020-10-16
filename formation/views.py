from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Formation, Inscrit_Formation
from .filters import FormationFilter
from accounts.models import Etudiant
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

def formation_list(request):
    formations_list = Formation.objects.all()
    myfilter = FormationFilter(request.GET,queryset=formations_list)
    formations_list = myfilter.qs
    context = {
        'formations' : formations_list,
        'myfilter' : myfilter
    }
    return render(request, 'formation_list.html', context)


def formation_detail(request, id):
    formation = Formation.objects.get(id=id)
    context = {
        'formation' : formation
    }
    return render(request, 'formation_detail.html', context)


@login_required
def inscription_formation(request, id):
    formation = Formation.objects.get(id=id)
    etudiant = Etudiant.objects.get(compte=request.user)
    test = Inscrit_Formation.objects.filter(etudiant=etudiant, formation=formation)
    if(len(test) == 0):
        inscrit_Formation = Inscrit_Formation(etudiant=etudiant, formation=formation)
        inscrit_Formation.save()
        context = {
            'formation' : formation
        }
        return redirect(reverse('accounts:mes_formations'))
    else:
        context = {
            'formation' : formation,
            'formation_erreur' : _('Vous être déjà inscrit à cette formation')
        }
        return render(request, 'formation_detail.html', context)
