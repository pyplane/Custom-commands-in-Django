from django.db import models

# Create your models here.

class Sample(models.Model):
    name = models.CharField(max_length=200)
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)