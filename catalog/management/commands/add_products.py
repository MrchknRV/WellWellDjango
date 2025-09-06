from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product

class Command(BaseCommand):
    help = 'Added test product to the BD'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        call_command('loaddata', 'test_product_fixture.json')