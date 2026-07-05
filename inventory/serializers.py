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

    #avec source='warehouse', Il va chercher product.warehouse → il obtient l'objet Python Warehouse complet (celui avec id, name, location, capacity)
    #Il passe cet objet à WarehouseSerializer pour le transformer en JSON
    #WarehouseSerializer regarde sa propre config (fields = ['id', 'name', 'location', 'capacity']) et transforme l'objet en ce JSON 
    # Nouveau champ : donne tous les détails de l'entrepôt, pas juste l'ID car le frontend pourrai vouloir afficher le nom de l'entrepot ca evitera d'appeler un autre api juste pour ca 
    #read_only=True veut dire : ce champ sert uniquement à afficher des données, jamais à en recevoir.
    warehouse_detail = WarehouseSerializer(source='warehouse', read_only=True)
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
            'warehouse_detail'
        ]

        #Avec read_only_fields, le champ status apparaît toujours dans les réponses JSON (en lecture), mais si quelqu'un essaie de l'envoyer dans une requête POST/PUT/PATCH, DRF l'ignore silencieusement.
        read_only_fields = ['status'] # Le status est en lecture seule dans le serializer, le frontend ne peut plus jamais le modifier via l'API car la mise à jour est automatique.




#Pourquoi serializers.Serializer et pas serializers.ModelSerializer ?
#ModelSerializer sert à représenter un modèle complet.
#Mais MoveProductSerializer ne représente aucun modèle — il ne sert qu'à valider une seule information ponctuelle : "quel est le nouvel entrepôt ?"
#C'est pour ça qu'il hérite directement de serializers.Serializer
class MoveProductSerializer(serializers.Serializer):
    """
    Serializer utilisé uniquement pour déplacer un produit.
    Il ne demande qu'une seule information :
    le nouvel entrepôt.
    """

    #Cette classe dit une seule chose : "J'attends UN champ, nommé warehouse, qui doit être l'ID d'un entrepôt qui existe réellement."
    warehouse = serializers.PrimaryKeyRelatedField(
        #queryset=Warehouse.objects.all() dit à DRF : "quand tu reçois un ID pour ce champ, va le chercher spécifiquement dans la table Warehouse — pas ailleurs."
        #Quand tu reçois une clé primaire, cherche-la uniquement parmi ces objets.
        queryset=Warehouse.objects.all()
    )