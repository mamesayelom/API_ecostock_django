from django.contrib import admin
from django.urls import path, include

# Import du router DRF
from rest_framework.routers import DefaultRouter

# Import des ViewSets
from inventory.views import ProductViewSet, WarehouseViewSet

# Création du router
router = DefaultRouter()

# Enregistrement des ressources API
router.register("products", ProductViewSet)
router.register("warehouses", WarehouseViewSet)

# URLs du projet
urlpatterns = [
    path('admin/', admin.site.urls),

    # On connecte toutes les routes API générées automatiquement
    path('api/', include(router.urls)),
]