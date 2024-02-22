import csv
import json
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from poi_manager.models import PointOfInterest

class Command(BaseCommand):
    help = 'Import PoI data from specified file(s)'

    def add_arguments(self, parser):
        parser.add_argument('file_paths', nargs='+', type=str, help='Path(s) to file(s) to import')

    def handle(self, *args, **kwargs):
        for file_path in kwargs['file_paths']:
            self.stdout.write(self.style.SUCCESS(f'Importing data from {file_path}...'))
            try:
                with open(file_path, 'r') as f:
                    # Determine file type based on extension
                    if file_path.endswith('.csv'):
                        self.import_csv(f)
                    elif file_path.endswith('.json'):
                        self.import_json(f)
                    elif file_path.endswith('.xml'):
                        self.import_xml(f)
                    else:
                        self.stdout.write(self.style.ERROR(f'Unsupported file format: {file_path}'))
            except FileNotFoundError:
                self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))

    def import_csv(self, file):
        reader = csv.DictReader(file)
        for row in reader:
            # Parse ratings as a set of values
            ratings_str = row['poi_ratings'].strip('{}')
            ratings = set(float(rating) for rating in ratings_str.split(','))

            # Calculate the average rating
            avg_rating = sum(ratings) / len(ratings) if ratings else 0.0

            poi = PointOfInterest(
                poi_id=row['poi_id'],
                poi_name=row['poi_name'],
                poi_latitude=float(row['poi_latitude']),
                poi_longitude=float(row['poi_longitude']),
                poi_category=row['poi_category'],
                poi_ratings=avg_rating  # Use the calculated average rating
            )
            poi.save()

    def import_json(self, file):
        data = json.load(file)
        for entry in data:
            # Parse ratings as a list of values
            ratings = entry.get('ratings', [])
            if isinstance(ratings, list):
                # Calculate the average rating
                avg_rating = sum(ratings) / len(ratings) if ratings else 0.0
            else:
                # If ratings is not a list, set avg_rating to 0
                avg_rating = 0.0

            poi = PointOfInterest(
                poi_id=entry['id'],
                poi_name=entry['name'],
                poi_latitude=float(entry['coordinates']['latitude']),
                poi_longitude=float(entry['coordinates']['longitude']),
                poi_category=entry['category'],
                poi_ratings=avg_rating  # Use the calculated average rating
            )
            poi.save()

    def import_xml(self, file):
        tree = ET.parse(file)
        root = tree.getroot()
        
        for record in root.findall('DATA_RECORD'):
            pid = record.find('pid').text
            pname = record.find('pname').text
            pcategory = record.find('pcategory').text
            platitude = float(record.find('platitude').text)
            plongitude = float(record.find('plongitude').text)
            pratings_str = record.find('pratings').text
            
            # Parse ratings as a list of values
            ratings = [float(rating) for rating in pratings_str.split(',')]
            
            # Calculate the average rating
            avg_rating = sum(ratings) / len(ratings) if ratings else 0.0
            
            poi = PointOfInterest(
                poi_id=pid,
                poi_name=pname,
                poi_latitude=platitude,
                poi_longitude=plongitude,
                poi_category=pcategory,
                poi_ratings=avg_rating
            )
            poi.save()
