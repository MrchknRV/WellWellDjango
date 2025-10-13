from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product
from config.settings import BASE_DIR


class Command(BaseCommand):
    help = "Added test product to the BD"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        call_command("loaddata", BASE_DIR / "fixtures/test_product_fixture.json")
