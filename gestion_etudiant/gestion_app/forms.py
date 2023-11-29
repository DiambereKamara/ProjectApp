from django import forms
from .models import Etudiant, Enseignant, AnneeScolaire, Groupe, Filiere, Module, Note, EmploisDuTemps, Bulletin

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = '__all__'

class AnneeScolaireForm(forms.ModelForm):
    class Meta:
        model = AnneeScolaire
        fields = '__all__'

class GroupeForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields = '__all__'

class FiliereForm(forms.ModelForm):
    class Meta:
        model = Filiere
        fields = '__all__'

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = '__all__'

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

class EmploisDuTempsForm(forms.ModelForm):
    class Meta:
        model = EmploisDuTemps
        fields = '__all__'

class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletin
        fields = '__all__'
