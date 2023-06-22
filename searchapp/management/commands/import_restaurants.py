import pandas as pd
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from searchapp.models import Dish


class Command(BaseCommand):
    help = 'Imports restaurant data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        df = pd.read_csv(csv_file)

        for _, row in df.iterrows():
            try:
                dish = Dish(
                    id=row['id'],
                    name=row['name'],
                    location=row['location'],
                    items=row['items'],
                    lat_long=row['lat_long'],
                    full_details=row['full_details']
                )
                dish.full_clean()  # Validate the model fields
                dish.save()
            except ValidationError as e:
                self.stdout.write(self.style.WARNING(f"Skipping invalid entry: {row['name']} ({e})"))

        self.stdout.write(self.style.SUCCESS('Restaurant data imported successfully!'))
