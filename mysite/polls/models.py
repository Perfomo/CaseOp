import collections
from django.db import models

# Create your models here.

class guns(models.Model):
    name = models.TextField(primary_key=True)
    collection = models.TextField()
    type = models.TextField()
    rarity = models.TextField()
    cost = models.TextField()
    gun_url = models.TextField()
    class Meta:
        db_table = 'guns'

class cases(models.Model):
    case_name = models.CharField(primary_key=True, max_length=50)
    case_logo_url = models.TextField()
    case_cost = models.TextField()
    class Meta:
        db_table = 'cases'