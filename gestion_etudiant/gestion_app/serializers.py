from rest_framework import serializers
from .models import Etudiant, Enseignant, AnneeScolaire, Groupe, Filiere, Module, Note, EmploisDuTemps, Bulletin

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'

class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignant
        fields = '__all__'

class AnneeScolaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnneeScolaire
        fields = '__all__'

class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupe
        fields = '__all__'

class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class EmploisDuTempsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploisDuTemps
        fields = '__all__'

class BulletinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bulletin
        fields = '__all__'
