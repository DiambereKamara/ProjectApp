from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    statut = models.CharField(max_length=50)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    email = models.EmailField()
    niveau_filiere = models.CharField(max_length=50)
    groupe = models.CharField(max_length=50)

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    matiere_enseignee = models.CharField(max_length=100)
    

class AnneeScolaire(models.Model):
    annee_debut = models.IntegerField()
    annee_fin = models.IntegerField()
   

class Groupe(models.Model):
    nom = models.CharField(max_length=50)
   

class Filiere(models.Model):
    nom = models.CharField(max_length=50)
 

class Module(models.Model):
    nom = models.CharField(max_length=50)
    
class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    valeur = models.DecimalField(max_digits=5, decimal_places=2)
   

class EmploisDuTemps(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    jour = models.CharField(max_length=20)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    

class Bulletin(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    annee_scolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE)
    moyenne_generale = models.DecimalField(max_digits=5, decimal_places=2)
    
