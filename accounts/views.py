from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from .forms import UserForm, EtudiantForm, UpdateUserForm, UpdateEtudiantForm
from django.urls import reverse
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from formation.models import Formation, Inscrit_Formation
from evenement.models import Evenement, Inscrit_evenement
from cours.models import Cours, Inscrit_cours
from .models import Etudiant, Commentaire

def index(request):
    context = {
        'hello' : _('Hello'),
    }
    return render(request,'accounts/index.html', context)

def inscription(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        etudiantform = EtudiantForm(request.POST)
        if userform.is_valid() and etudiantform.is_valid():
            user = userform.save()
            etudiant = etudiantform.save(False)

            etudiant.compte = user 
            etudiant.save()

            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password1']
            user = authenticate(username= username, password= password)
            login(request, user)
            return redirect('/accounts/profile')
        return render(request, 'registration/register.html',{'userform':userform, 'etudiantform':etudiantform})
    else:
        userform = UserForm()
        etudiantform = EtudiantForm()
        return render(request, 'registration/register.html',{'userform':userform, 'etudiantform':etudiantform})

@login_required
def profile(request):
    etudiant = Etudiant.objects.get(compte=request.user)
    return render(request, 'accounts/profile.html', {'etudiant':etudiant})

@login_required
def profil_edit(request):
    etudiant = Etudiant.objects.get(compte=request.user)
    if request.method == 'POST':
        try:
            updateuserform = UpdateUserForm(request.POST, instance= request.user)
            updateetudiantform = UpdateEtudiantForm(request.POST, request.FILES, instance= etudiant)
            if updateuserform.is_valid() and updateetudiantform.is_valid():
                updateuserform.save()
                monprofil = updateetudiantform.save(commit=False)
                monprofil.compte = request.user
                monprofil.save()
                return redirect(reverse('accounts:profil_edit'))
            return render(request, 'accounts/user.html', {'etudiant':etudiant, 'updateuserform':updateuserform, 'updateetudiantform':updateetudiantform})
        except:
            return render(request, 'accounts/user.html', {'msgerror': "l'image invalide"})
    else:
        updateuserform = UpdateUserForm(instance = request.user)
        updateetudiantform = UpdateEtudiantForm(instance = etudiant)
    return render(request, 'accounts/user.html', {'etudiant':etudiant, 'updateuserform':updateuserform, 'updateetudiantform':updateetudiantform})

@login_required
def mes_cours(request):
    etudiant = Etudiant.objects.get(compte = request.user)
    try:
        mes_cours = Inscrit_cours.objects.filter(etudiant = etudiant)
        context = {'mes_cours':mes_cours}
    except Inscription_cours.DoesNotExist:
        context = {}
    
    return render(request, 'accounts/mes_cours.html', context)

@login_required
def mes_formations(request):
    etudiant = Etudiant.objects.get(compte = request.user)
    try:
        mes_formations = Inscrit_Formation.objects.filter(etudiant = etudiant)
        context = {'mes_formations':mes_formations}
    except Inscrit_Formation.DoesNotExist:
        context = {}
    
    return render(request, 'accounts/mes_formations.html', context)

@login_required
def mes_evenements(request):
    etudiant = Etudiant.objects.get(compte = request.user)
    try:
        mes_evenements = Inscrit_evenement.objects.filter(etudiant = etudiant)
        context = {'mes_evenements':mes_evenements}
    except Inscription_evenement.DoesNotExist:
        context = {}
    
    return render(request, 'accounts/mes_evenements.html', context)


@login_required
def mon_avis(request):
    etudiant = Etudiant.objects.get(compte=request.user)
    if request.method == 'POST':
        nbrEtoiles = request.POST['nbrEtoiles']
        commentaire = request.POST['commentaire']
        if Commentaire.objects.filter(proprietaire=etudiant).exists():
            commentaireObj = Commentaire.objects.get(proprietaire=etudiant)
            commentaireObj.commentaire = commentaire
            commentaireObj.nbrEtoiles = nbrEtoiles    
        else:
            commentaireObj = Commentaire(proprietaire=etudiant, commentaire=commentaire,nbrEtoiles=nbrEtoiles)

        commentaireObj.acceptable = False
        commentaireObj.save()
    else:
        if Commentaire.objects.filter(proprietaire=etudiant).exists():
            commentaireObj = Commentaire.objects.get(proprietaire=etudiant)
        else:
            commentaireObj = {} 
    return render(request, 'accounts/mon_avis.html', {'etudiant':etudiant, 'commentaire':commentaireObj})