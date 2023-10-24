from django.core.management import BaseCommand

from homework2.models import Customer


class Command(BaseCommand):
    help = "Get all customers."

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()

        self.stdout.write(f'Customers list:\n{customers}')
