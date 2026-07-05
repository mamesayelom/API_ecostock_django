# products/management/commands/update_expired_products.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from inventory.models import Product

class Command(BaseCommand):
    help = "Marque comme périmés tous les produits dont la date est dépassée"

    def handle(self, *args, **options):
        today = timezone.now().date()
        updated = Product.objects.filter(
            expiration_date__lt=today
        ).exclude(
            status=Product.EXPIRED
        ).exclude(
            status=Product.RESERVED  # règle métier : on ne touche pas aux réservés
        ).update(status=Product.EXPIRED)

        self.stdout.write(f"{updated} produit(s) marqué(s) comme périmé(s)")