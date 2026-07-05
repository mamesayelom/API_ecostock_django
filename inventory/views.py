from rest_framework.viewsets import ModelViewSet
from .models import Product,Warehouse
from .serializers import ProductSerializer,WarehouseSerializer


class WarehouseViewSet(ModelViewSet):

    # Les données sur lesquelles on travaille
    queryset = Warehouse.objects.all()

    # Comment transformer les données en JSON
    serializer_class = WarehouseSerializer


class ProductViewSet(ModelViewSet):

    # Les données sur lesquelles on travaille
    queryset = Product.objects.all()

    # Comment transformer les données en JSON
    serializer_class = ProductSerializer
