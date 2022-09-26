from django.db import models

from plants.models import Plant

class Cell(models.Model):
  code = models.CharField(max_length=6, unique=True, blank=False, null=False)
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)