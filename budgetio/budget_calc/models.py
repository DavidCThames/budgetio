from django.db import models

# Create your models here.
class Expenceses(models.Model):
    salary = models.IntegerField()
    food = models.IntegerField()
    housing = models.IntegerField()
    transportation = models.IntegerField()
    healthcare = models.IntegerField()
    taxes = models.IntegerField()
    other = models.IntegerField()

class Neighborhoods(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longtitude = models.CharField(max_length=50)
    restaurants = model.ForeignKey(Restaurants, on_delete=models.CASCADE)

class Restaurants(models.Model):
    name = models.CharField(max_length=50)
    price_range =  models.IntegerField()
    latitude =  models.DecimalField()
    longtitude = models.DecimalField()
    photos_url = models.CharField(max_length=150) 
    user_rating = models.DecimalField(max_digits=1, decimal_places=1)
    cuisines = models.CharField(max_length=150)
    has_online_delivery = models.IntegerField()





