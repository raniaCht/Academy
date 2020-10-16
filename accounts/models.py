from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import django.db.models.deletion
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

GENRES = [
    ('HOMME', _('Homme')),
    ('FEMME', _('Femme')),
] 

def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "profils/%s_%s.%s"%(instance.compte, datetime.now().strftime("%Y%m%d_%H%M%S"), extension)

class Etudiant(models.Model):
    compte = models.OneToOneField(User, on_delete=models.CASCADE)
    dateDeNais = models.DateField()
    genre = models.CharField(max_length=10, choices=GENRES)
    image = models.ImageField(upload_to=image_upload, default='default.png')

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="/media/%s" width="48" height="48" style="border-radius:25px;" />' % (self.image)) 
        else:
            return mark_safe('<img src="/media/default.png" width="48" height="48" style="border-radius:25px;background-color: #fefbd8;" />')

class Commentaire(models.Model):    
    proprietaire = models.OneToOneField(Etudiant, on_delete=models.CASCADE)
    commentaire = models.TextField(max_length=2000, default='')
    nbrEtoiles = models.IntegerField(default=1)
    acceptable = models.BooleanField(default=False)