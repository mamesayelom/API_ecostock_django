from rest_framework.viewsets import ModelViewSet
from .models import Product,Warehouse
from .serializers import ProductSerializer,WarehouseSerializer,MoveProductSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


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



    #Quel est le problème qu'on veut resoudre: On veut pouvoir déplacer un produit d'un entrepôt à un autre.
    #Quelles informations me faut-il pour effectuer cette action ?
    # - Quel produit ?
    # - Vers quel entrepôt ?
    #Comment le frontend va me transmettre ces informations ?
    #via l'url /api/products/pk/move/ creer par router je connaitrais l'id du produit en question et dans le body j'aurai {"warehouse": 2} qui sera l'entrepot en question
    #Dans quels cas dois-je refuser cette action ?
    #si le produit est périmé → refus
    #si l'entrepôt n'existe pas → refus
    #si le produit n'existe pas → 404
    #si l'utilisateur n'est pas connecté → 401
    #si l'utilisateur n'a pas le droit → 403
    @action(detail=True, methods=['post'])
    def move(self, request, pk=None):
         # Récupérer l'objet produit concerné(sert à récupérer l’objet lié au pk dans l’URL)
         #get_object() utilise en interne :get_object_or_404(Produit,pk=pk)
        product = self.get_object()

        if product.status == Product.EXPIRED:
            return Response(
                {
                    "error": "Ce produit est périmé et ne peut pas être déplacé"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        # Récupérer le nouvel entrepôt envoyé par le frontend
        #request.data est un dictionnaire python et la méthode .get() d'un dictionnaire sert à récupérer la valeur associée à une clé donc si tu fais data.get("warehouse") il donnera la valeur de la cette clee.
        #new_warehouse_id = request.data.get("warehouse")

        # Vérification
        #if not new_warehouse_id:
            #return Response(
                #{"error": "warehouse est requis"},
                #status=status.HTTP_400_BAD_REQUEST
            #)
        
        # Mise à jour du produit
        #product.warehouse_id = new_warehouse_id
        #product.save()
        serializer = MoveProductSerializer(data=request.data)
        #avec raise_exception=True, is_valid() ne renvoie pas False s'il y'a une erreur. Elle lève directement une exception (ValidationError)
        serializer.is_valid(raise_exception=True)
        #serializer.validated_data garde les donnees valider(dict)
        product.warehouse = serializer.validated_data["warehouse"]
        product.save()


        # Réponse API
        return Response(
            {
                "message": "Produit déplacé avec succès",
                "product": ProductSerializer(product).data
            },
            status=status.HTTP_200_OK
        )


   

        







#Dans DRF, ModelViewSet te donne uniquement les actions CRUD :( list	GET /products/,   retrieve	GET /products/1/,    create	  POST /products/	,   update	  PUT /products/1/,   destroy	DELETE /products/1/)

#Mais le projet Eco-Stock a besoin de plus : déplacer un produit d’un entrepôt à un autre, marquer un produit comme périmé automatiquement, faire un audit de stock

#Le décorateur @action permet de : créer des endpoints personnalisés dans un ViewSet car ModelViewSet = générique (CRUD uniquement)

#nb: C’est toujours le Router (DefaultRouter) qui crée les routes avec @action. il détecte automatiquement les méthodes décorées avec @action

