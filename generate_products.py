from django.core.management.base import BaseCommand
from faker import Faker
from products.models import *


class Command(BaseCommand):
    help = "Generate fake products"

    def add_arguments(self, parser):
        parser.add_argument(
            "number", type=int, help="Indicates the number of products to be created"
        )

    def handle(self, *args, **kwargs):
        number = kwargs["number"]
        fake = Faker()

        for _ in range(number):
            title = fake.sentence(nb_words=6)
            content = fake.paragraph(nb_sentences=3)
            price = fake.random_int(min=10, max=1000)

            Product.objects.create(title=title, content=content, price=price)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully generated {number} fake products")
        )
