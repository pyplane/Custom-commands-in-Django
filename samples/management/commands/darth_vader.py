from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'run in order to join the dark side'

    def handle(self, *args, **options):
        print('please like, subscribe & comment')