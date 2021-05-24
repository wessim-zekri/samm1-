from django.db import models
from django.contrib.auth.models import User


class Employé(models.Model):
    session_user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    telephone = models.PositiveIntegerField(null=True)
    email = models.EmailField(max_length=100, null=True)
    adresse = models.CharField(max_length=200, null=True)
    titre = models.CharField(max_length=200, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return u"%s %s " % (self.nom, self.prenom)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Employé.objects.create(user=instance)


class Projet(models.Model):
    ETAT = (
        ('Terminé', 'Terminé'),
        ('En cours', 'En cours'),
        ('Suspendu', 'Suspendu'),
    )
    designation = models.CharField(max_length=200, null=True)
    responsable = models.CharField(max_length=200, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
    durée_en_semaines = models.PositiveIntegerField(null=True)
    statut = models.CharField(max_length=200, null=True, choices=ETAT)

    def __str__(self):
        return self.designation

class Fabricant(models.Model):
    nom = models.CharField(max_length=200, null=True)
    reference = models.CharField(max_length=200, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom

class Piece(models.Model):
    CATEGORY = (
        ('Electrique', 'Electrique'),
        ('Mecanique', 'Mecanique'),
    )
    designation = models.CharField(max_length=200, null=True)
    reference = models.CharField(max_length=200, null=True)
    categorie = models.CharField(max_length=200, null=True, choices=CATEGORY)
    prix = models.FloatField(default=0.0, null=True)
    fabricant = models.ForeignKey(Fabricant, null=True, on_delete= models.SET_NULL) 
    date_creation = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.designation

class Fournisseur(models.Model):
    nom = models.CharField(max_length=200, null=True)
    reference = models.CharField(max_length=200, null=True)
    telephone = models.PositiveIntegerField(null=True)
    email = models.EmailField(max_length=100, null=True)
    adresse = models.CharField(max_length=200, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
    pieces = models.ForeignKey(Piece, null=True, on_delete= models.SET_NULL) 
    def __str__(self):
        return self.nom

'''class Tag(models.Model):
    designation = models.CharField(max_length=200, null=True)'''

class Demande(models.Model):
    ETAT = (
        ('Validée', 'Validée'),
        ('Non Validée', 'Non Validée'),
    )
    projet = models.ForeignKey(Projet, null=True, on_delete= models.SET_NULL)  
    piece = models.ForeignKey(Piece, null=True, on_delete= models.SET_NULL)
    reference_piece = models.CharField(max_length=200, null=True)
    quantite_piece = models.PositiveIntegerField(default=1, null=True)
    fabricant = models.ForeignKey(Fabricant, null=True, on_delete= models.SET_NULL)  
    reference_fabricant = models.CharField(max_length=200, null=True)   
    fournisseur = models.ForeignKey(Fournisseur, null=True, on_delete= models.SET_NULL)  
    reference_fournisseur = models.CharField(max_length=200, null=True)
    statut = models.CharField(max_length=200, null=True, choices=ETAT, blank=True)
    commentaire = models.TextField(max_length=200, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
    #tags = models.ManyToManyField(Tag)

class Demande_Validée(models.Model):
    demande = models.ForeignKey(Demande, null=True, on_delete= models.SET_NULL)
    validateur = models.ForeignKey(Employé, null=True, on_delete= models.SET_NULL)
    date_validation =  models.DateTimeField(auto_now_add=True, null=True)

class Demande_Non_Validée(models.Model):
    demande = models.ForeignKey(Demande, null=True, on_delete= models.SET_NULL)
    rejeteur = models.ForeignKey(Employé, null=True, on_delete= models.SET_NULL)
    date_rejection =  models.DateTimeField(auto_now_add=True, null=True)

class Commande(models.Model):
    ETAT = (
        ('Livrée', 'Livrée'),
        ('En cours', 'En cours'),
        ('En retard', 'En retard'),
        ('Annulée', 'Annulée'),
    )
    demande = models.ForeignKey(Demande, null=True, on_delete= models.SET_NULL,blank=True)
    fournisseur = models.ForeignKey(Fournisseur, null=True, on_delete= models.SET_NULL)
    statut = models.CharField(max_length=200, null=True, choices=ETAT)
    date_commande = models.DateTimeField(auto_now_add=True, null=True)
    date_livraison = models.CharField(max_length=200, null=True)