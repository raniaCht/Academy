from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Cours, Inscrit_cours
from .filters import CoursFilter
from accounts.models import Etudiant


def cours_list(request):
    cours_list = Cours.objects.all()
    myfilter = CoursFilter(request.GET,queryset=cours_list)
    cours_list = myfilter.qs
    context = {
        'cours' : cours_list,
        'myfilter' : myfilter
    }
    return render(request, 'cours_list.html', context)

def cours_detail(request, id):
    cours = Cours.objects.get(id=id)
    context = {
        'cours' : cours
    }
    return render(request, 'cours_detail.html', context)


@login_required
def inscription_cours(request, id):
    cours = Cours.objects.get(id=id)
    etudiant = Etudiant.objects.get(compte=request.user)
    test = Inscrit_cours.objects.filter(etudiant=etudiant, cours=cours)
    if(len(test) == 0):
        inscrit_cours = Inscrit_cours(etudiant=etudiant, cours=cours)
        inscrit_cours.save()
        return redirect(reverse('accounts:mes_cours'))
    else:
        context = {
            'cours' : cours,
            'cours_erreur' : _('Vous être déjà inscrit à cette cours')
        }
        return render(request, 'cours_detail.html', context)
