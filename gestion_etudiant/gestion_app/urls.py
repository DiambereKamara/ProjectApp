from django.urls import path
from .views import EtudiantListCreateView, EnseignantListCreateView, AnneeScolaireListCreateView, GroupeListCreateView, FiliereListCreateView, ModuleListCreateView, NoteListCreateView, EmploisDuTempsListCreateView, BulletinListCreateView

urlpatterns = [
    path('etudiant/', EtudiantListCreateView.as_view(), name='etudiant-list-create'),
    path('enseignant/', EnseignantListCreateView.as_view(), name='enseignant-list-create'),
    path('annee-scolaire/', AnneeScolaireListCreateView.as_view(), name='annee-scolaire-list-create'),
    path('groupe/', GroupeListCreateView.as_view(), name='groupe-list-create'),
    path('filiere/', FiliereListCreateView.as_view(), name='filiere-list-create'),
    path('module/', ModuleListCreateView.as_view(), name='module-list-create'),
    path('note/', NoteListCreateView.as_view(), name='note-list-create'),
    path('emplois-du-temps/', EmploisDuTempsListCreateView.as_view(), name='emplois-du-temps-list-create'),
    path('bulletin/', BulletinListCreateView.as_view(), name='bulletin-list-create'),
]
