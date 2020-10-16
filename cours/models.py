from django.db import models
from django.utils.translation import gettext as _
from accounts.models import Etudiant

NIVEAUX = [
    ('Prepremaire',_('Pre Primary')),
    ('Premaire', _('Primary')),
    ('Moyen', _('Middle')),
    ('Lycee', _('Secondary')),
    ('Universitaire', _('University'))
]


class Niveau_scolaire(models.Model):
    nom = models.CharField(max_length=15, choices=NIVEAUX, unique=True)


    def __str__(self):
        return self.nom

ANNEES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
]

class Annee(models.Model):
    nom = models.IntegerField(choices=ANNEES, unique=True)

    def __str__(self):
        return str(self.nom)


class Matiere(models.Model):
    nom = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nom

 
class Cours(models.Model):
    niveau = models.ForeignKey(Niveau_scolaire, on_delete=models.CASCADE)
    annee = models.ForeignKey(Annee, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    prix = models.IntegerField()
    description = models.TextField(max_length=1000, default=' ')


class Inscrit_cours(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)

    class Meta:
        unique_together=(
            ('etudiant', 'cours'),
        )