from django.db import models
from django.utils import timezone

# Modèle représentant un entrepôt de stockage
class Warehouse(models.Model):

    # Nom de l'entrepôt (ex: Entrepôt Dakar)
    name = models.CharField(max_length=255)

    # Localisation géographique (ex: Pikine, Dakar)
    location = models.CharField(max_length=255)

    # Capacité maximale de stockage (nombre de produits ou volume)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        # Permet d'afficher un Warehouse de façon lisible dans l'admin
        return self.name
    

class Product(models.Model):

    # Nom du produit (ex: Lait, Riz, Pain)
    name = models.CharField(max_length=255)

    # Quantité disponible dans le stock
    quantity = models.PositiveIntegerField()

    # Date d'expiration du produit
    expiration_date = models.DateField()

    # États possibles du produit
    AVAILABLE = "available"
    RESERVED = "reserved"
    EXPIRED = "expired"

    STATUS_CHOICES = [
        (AVAILABLE, "Disponible"),
        (RESERVED, "Réservé"),
        (EXPIRED, "Périmé"),
    ]

    # État actuel du produit
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=AVAILABLE
    )

    # Relation : un produit appartient à un entrepôt
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="products"
    )

    def __str__(self):
        return self.name
    
    #Le save() ne se déclenche que si quelqu'un modifie le produit(une méthode qu'on appelle avant de sauvegarder)
    #Mais un produit peut dépasser sa date de péremption un jour où personne ne le touche
    def save(self, *args, **kwargs):
        # Sécurité : si le produit est périmé à la date du jour,
        # on force le statut, sauf s'il était déjà "reserved"
        # (à adapter selon ta règle métier exacte)
        if self.expiration_date < timezone.now().date() and self.status != self.RESERVED:
            self.status = self.EXPIRED
        super().save(*args, **kwargs)
