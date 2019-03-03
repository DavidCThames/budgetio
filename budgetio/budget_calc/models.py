from django.db import models

# Create your models here.
class Expences(models.Model):
    salary = models.IntegerField()
    food = models.IntegerField()
    housing = models.IntegerField()
    transportation = models.IntegerField()
    healthcare = models.IntegerField()
    taxes = models.IntegerField()
    other = models.IntegerField()

class Restaurants(models.Model):
    name = models.CharField(max_length=50)
    price_range =  models.IntegerField()
    latitude =  models.CharField(max_length=50)
    longtitude = models.CharField(max_length=50)
    photos_url = models.CharField(max_length=150) 
    user_rating = models.DecimalField(max_digits=1, decimal_places=1)
    cuisines = models.CharField(max_length=150)
    has_online_delivery = models.IntegerField()

class Neighborhoods(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longtitude = models.CharField(max_length=50)
    cost = models.IntegerField()
    photo_url = models.CharField(max_length=150) 
    description = models.CharField(max_length=500)
    r1 = models.ForeignKey(Restaurants, related_name='Restaurant1', on_delete=models.CASCADE)
    r2 = models.ForeignKey(Restaurants, related_name='Restaurant2', on_delete=models.CASCADE)
    r3 = models.ForeignKey(Restaurants, related_name='Restaurant3', on_delete=models.CASCADE)
    r4 = models.ForeignKey(Restaurants, related_name='Restaurant4', on_delete=models.CASCADE)
