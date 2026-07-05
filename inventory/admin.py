from django.contrib import admin

from .models import Warehouse, Product

# Enregistrement du modèle Warehouse dans l'interface admin
@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ('id', 'name', 'location', 'capacity')

    # Permet de rechercher par nom et localisation
    search_fields = ('name', 'location')


# Enregistrement du modèle Product dans l'interface admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste des produits
    list_display = ('id', 'name', 'quantity', 'status', 'warehouse')

    # Filtrer les produits par état
    list_filter = ('status', 'warehouse')

    # Recherche rapide par nom
    search_fields = ('name',)
