from django.core.management import BaseCommand

from homework2.models import Order


class Command(BaseCommand):
    help = "Get all orders."

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()

        self.stdout.write(f'Orders list:\n{orders}')
