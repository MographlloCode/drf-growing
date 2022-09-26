from django.db import models

class Plant(models.Model):
  code = models.CharField(max_length=6, unique=True, blank=False, null=False)
  name = models.CharField(max_length=255)
  temperature = models.DecimalField(max_digits=4, decimal_places=2)
  watering_week = models.IntegerField()
  description = models.TextField(default="")
