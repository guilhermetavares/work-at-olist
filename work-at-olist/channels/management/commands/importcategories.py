from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Import categories from csv'

    def add_arguments(self, parser):
        parser.add_argument('channel', nargs='+', type=str)
        parser.add_argument('csv_path', nargs='+', type=str)

    def handle(self, *args, **options):
        pass
        print(args, options)
