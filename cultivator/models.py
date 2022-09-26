from django.db import models

class Cultivator(models.Model):
  username = models.CharField(max_length=255, unique=True, blank=False, null=False)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
  password = models.CharField(max_length=50)