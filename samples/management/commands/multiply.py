from django.core.management.base import BaseCommand
from samples.models import Sample

class Command(BaseCommand):
    help = 'Multiply the total count by a param'

    def add_arguments(self, parser):
        parser.add_argument('param', type=int)

    def handle(self, *args, **options):
        param = options.get('param')
        count = Sample.objects.all().count()
        multiply = count * param
        print(multiply)