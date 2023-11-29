from rest_framework import generics
from .models import Etudiant, Enseignant, AnneeScolaire, Groupe, Filiere, Module, Note, EmploisDuTemps, Bulletin
from .serializers import EtudiantSerializer, EnseignantSerializer, AnneeScolaireSerializer, GroupeSerializer, FiliereSerializer, ModuleSerializer, NoteSerializer, EmploisDuTempsSerializer, BulletinSerializer

class EtudiantListCreateView(generics.ListCreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

class EnseignantListCreateView(generics.ListCreateAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer

class AnneeScolaireListCreateView(generics.ListCreateAPIView):
    queryset = AnneeScolaire.objects.all()
    serializer_class = AnneeScolaireSerializer

class GroupeListCreateView(generics.ListCreateAPIView):
    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer

class FiliereListCreateView(generics.ListCreateAPIView):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer

class ModuleListCreateView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class EmploisDuTempsListCreateView(generics.ListCreateAPIView):
    queryset = EmploisDuTemps.objects.all()
    serializer_class = EmploisDuTempsSerializer

class BulletinListCreateView(generics.ListCreateAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer

