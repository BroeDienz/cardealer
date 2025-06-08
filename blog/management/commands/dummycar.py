import csv
from decimal import Decimal
from django.core.management.base import BaseCommand
from blog.models import Car
import os

class Command(BaseCommand):
    help = 'Load dummy car data from a CSV file'

    def handle(self, *args, **kwargs):
        # Input the CSV file
        csv_file_path = input("Enter the path to the CSV file: ")
        
        # Check if the file exists
        if not os.path.isfile(csv_file_path):
            self.stdout.write(self.style.ERROR(f"File {csv_file_path} does not exist."))
            return
        
        # Open the CSV file and read its content
        with open(csv_file_path, 'r' , newline="") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            count = 0
            
            for row in reader:
                # Create a new Car object for each row in the CSV
                try:
                    Car.objects.create(
                        id=int(row['id']),
                        register=row['Register'],
                        make=row['make'],
                        model=row['model'],
                        price=Decimal(row['price']),
                        year=int(row['year']),
                        vin=row['vin'],
                    )
                    count += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error creating car: {e}"))
                
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {count} cars from {csv_file_path}'))   