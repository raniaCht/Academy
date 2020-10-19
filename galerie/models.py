from django.db import models
from formation.models import Formation
from evenement.models import Evenement
from datetime import datetime

def photo_formation(instance, filename):
    imagename, extension = filename.split(".")
    return "formations__images/%s_%s.%s"%(instance.id, datetime.now().strftime("%Y%m%d_%H%M%S"), extension)

class Galerie_Formation(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=photo_formation, null=False)



def photo_evenement(instance, filename):
    imagename, extension = filename.split(".")
    return "evenements__images/%s_%s.%s"%(instance.id, datetime.now().strftime("%Y%m%d_%H%M%S"), extension)

class Galerie_Evenement(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=photo_evenement, null=False)
