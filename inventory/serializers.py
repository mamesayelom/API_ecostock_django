from rest_framework import serializers
from .models import Warehouse
from .models import Product

# Serializer = traducteur entre objet Python (Warehouse)
# et format JSON utilisé par le frontend
class WarehouseSerializer(serializers.ModelSerializer):

    # Meta classe = configuration du serializer
    class Meta:

        # On indique le modèle à transformer
        model = Warehouse

        # On choisit les champs à exposer dans l'API. Si un champ n’est pas ici → il n’apparaît pas dans l’API
        fields = [
            'id',        # identifiant automatique
            'name',      # nom de l'entrepôt
            'location',  # localisation
            'capacity'   # capacité de stockage
        ]




# Serializer du modèle Product
# Sert à transformer Product ↔ JSON + validation des données
class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        # On précise le modèle à utiliser
        model = Product

        # Champs exposés dans l'API
        fields = [
            'id',               # identifiant du produit
            'name',             # nom du produit
            'quantity',         # quantité en stock
            'expiration_date',  # date de péremption
            'status',           # état du produit (available, reserved, expired)
            'warehouse',       # relation vers Warehouse (via id)
        ]