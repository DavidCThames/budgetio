from django.db import models

# Create your models here.
class ExpencesLookupTable(models.Model):
    salary = models.IntegerField()
    food = models.IntegerField()
    housing = models.IntegerField()
    transportation = models.IntegerField()
    healthcare = models.IntegerField()
    taxes = models.IntegerField()
    other = models.IntegerField()


