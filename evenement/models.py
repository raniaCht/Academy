from django.db import models
from datetime import datetime
from accounts.models import Etudiant


class Evenement(models.Model):
    titre = models.CharField(max_length=100)
    lieu = models.CharField(max_length=100)
    date_et_heure = models.DateTimeField()
    formatteur = models.CharField(max_length=30)

    def __str__(self):
        return self.titre

class Inscrit_evenement(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)

    class Meta:
        unique_together=(
            ('etudiant', 'evenement'),
        )