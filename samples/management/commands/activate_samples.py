from django.core.management.base import BaseCommand
from samples.models import Sample

class Command(BaseCommand):
    help = 'activate all unactive samples'

    def handle(self, *args, **options):
        size = Sample.objects.filter(activated=False).count()
        if size != 0:
            qs = Sample.objects.filter(activated=False)
            count = 0
            for obj in qs:
                count += 1
                obj.activated = True
                obj.save()
            print(f"activated {count}")
        else:
            print('Nothing here to do...')