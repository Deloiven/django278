from django.core.management import BaseCommand

from homework2.models import Product


class Command(BaseCommand):
    help = "Get all products."

    def handle(self, *args, **kwargs):
        products = Product.objects.all()

        self.stdout.write(f'Products list:\n{products}')
