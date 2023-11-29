from django.contrib import admin
from .models import Etudiant, Enseignant, AnneeScolaire, Groupe, Filiere, Module, Note, EmploisDuTemps, Bulletin

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'date_naissance']
    search_fields = ['nom', 'prenom']

@admin.register(Enseignant)
class EnseignantAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'matiere_enseignee']
    search_fields = ['nom', 'prenom']

@admin.register(AnneeScolaire)
class AnneeScolaireAdmin(admin.ModelAdmin):
    list_display = ['annee_debut', 'annee_fin']
    search_fields = ['annee_debut']

@admin.register(Groupe)
class GroupeAdmin(admin.ModelAdmin):
    list_display = ['nom']
    search_fields = ['nom']

@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ['nom']
    search_fields = ['nom']

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['nom']
    search_fields = ['nom']

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['etudiant', 'module', 'valeur']
    search_fields = ['etudiant__nom', 'module__nom']

@admin.register(EmploisDuTemps)
class EmploisDuTempsAdmin(admin.ModelAdmin):
    list_display = ['enseignant', 'module', 'jour', 'heure_debut', 'heure_fin']
    search_fields = ['enseignant__nom', 'module__nom']

@admin.register(Bulletin)
class BulletinAdmin(admin.ModelAdmin):
    list_display = ['etudiant', 'annee_scolaire', 'moyenne_generale']
    search_fields = ['etudiant__nom', 'annee_scolaire__annee_debut']

