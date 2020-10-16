from django.db import models
from django.utils.translation import gettext as _
from accounts.models import Etudiant

class Categorie(models.Model):
    nom = models.CharField(max_length=50)


    def __str__(self):
        return self.nom


class Niveau(models.Model):
    niveau = models.CharField(max_length=10)

    def __str__(self):
        return self.niveau


TYPES_FORMATION = [
    ('GOLD', _('Gold')),
    ('NORMAL', _('Normal')),
]

class Formation(models.Model):
    nom = models.CharField(max_length=20)
    formation_type = models.CharField(max_length=20, choices=TYPES_FORMATION)
    description = models.TextField(max_length=1000, default=' ')
    prix = models.IntegerField()
    date_deb = models.DateField()
    date_fin = models.DateField()
    duree_en_h = models.IntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nom



class Inscrit_Formation(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
   
    class Meta:
        unique_together = (
            ("etudiant", "formation"),
        )
