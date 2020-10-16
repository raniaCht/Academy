from django.forms import ModelForm, DateInput, ChoiceField, Select, CharField, TextInput
from django.contrib.auth.forms import UserCreationForm
from .models import Etudiant
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = ['genre', 'dateDeNais']
        widgets = {'dateDeNais': DateInput(attrs={'id': 'datepicker'}), 'genre' : Select(attrs={'id':'select-input'}) }

class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UpdateEtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = ['image']