from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, null=True, blank=True)
    

class Matiere(models.Model):
    nom = models.CharField(max_length=100, null=True, blank=True)
    categorie = models.ForeignKey(Categorie, null=True, blank=True, on_delete=models.CASCADE)


class Cours(models.Model):
    titre = models.CharField(max_length=100, null=True, blank=True)
    chapitre = models.IntegerField(null=True, blank=True)
    matiere = models.ForeignKey(Matiere, null=True, blank=True, on_delete=models.CASCADE)




class Enseignant(models.Model):
    pass


class Apprenant(models.Model):
    pass