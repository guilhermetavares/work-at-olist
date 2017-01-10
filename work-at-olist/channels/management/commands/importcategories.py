from django.core.management.base import BaseCommand, CommandError
from utils.import_data import make_channel_data

class Command(BaseCommand):
    help = '''Import categories from csv.
            ex. manage.py importcategories channel_name path/of/the/csv/file.csv 
            or manage.py importcategories channel_name url_of_csv'''

    def add_arguments(self, parser):
        parser.add_argument('channel')
        parser.add_argument('csv_path')

    def handle(self, *args, **options):
        channel = options['channel']
        csv_path = options['csv_path']
        response = make_channel_data(channel, csv_path)
        self.stdout.write("Command 'importcategories' executed with status: '{0}'' message: '{1}'".format(
            response.get('status'), response.get('message')))


