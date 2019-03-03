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
    name = models.CharField(max_length=50, default=None, blank=True, null=True)
    price_range =  models.IntegerField(default=None, blank=True, null=True)
    latitude =  models.CharField(max_length=50, default=None, blank=True, null=True)
    longitude = models.CharField(max_length=50, default=None, blank=True, null=True)
    photos_url = models.CharField(max_length=150, default=None, blank=True, null=True) 
    user_rating = models.DecimalField(max_digits=10, decimal_places=1, default=None, blank=True, null=True)
    cuisines = models.CharField(max_length=150, default=None, blank=True, null=True)
    has_online_delivery = models.IntegerField(default=None, blank=True, null=True)

class Neighborhoods(models.Model):
    name = models.CharField(max_length=50, default=None, blank=True, null=True)
    latitude = models.CharField(max_length=50, default=None, blank=True, null=True)
    longitude = models.CharField(max_length=50, default=None, blank=True, null=True)
    cost = models.IntegerField(default=None, blank=True, null=True)
    photo_url = models.CharField(max_length=150, default=None, blank=True, null=True) 
    description = models.CharField(max_length=500, default=None, blank=True, null=True)

    r1_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    r1_price_range =  models.IntegerField(default=None, blank=True, null=True)
    r1_latitude =  models.CharField(max_length=50, default=None, blank=True, null=True)
    r1_longitude = models.CharField(max_length=50, default=None, blank=True, null=True)
    r1_photos_url = models.CharField(max_length=150, default=None, blank=True, null=True) 
    r1_user_rating = models.DecimalField(max_digits=10, decimal_places=1, default=None, blank=True, null=True)
    r1_cuisines = models.CharField(max_length=150, default=None, blank=True, null=True)
    r1_has_online_delivery = models.IntegerField(default=None, blank=True, null=True)

    r2_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    r2_price_range =  models.IntegerField(default=None, blank=True, null=True)
    r2_latitude =  models.CharField(max_length=50, default=None, blank=True, null=True)
    r2_longitude = models.CharField(max_length=50, default=None, blank=True, null=True)
    r2_photos_url = models.CharField(max_length=150, default=None, blank=True, null=True) 
    r2_user_rating = models.DecimalField(max_digits=10, decimal_places=1, default=None, blank=True, null=True)
    r2_cuisines = models.CharField(max_length=150, default=None, blank=True, null=True)
    r2_has_online_delivery = models.IntegerField(default=None, blank=True, null=True)

    r3_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    r3_price_range =  models.IntegerField(default=None, blank=True, null=True)
    r3_latitude =  models.CharField(max_length=50, default=None, blank=True, null=True)
    r3_longitude = models.CharField(max_length=50, default=None, blank=True, null=True)
    r3_photos_url = models.CharField(max_length=150, default=None, blank=True, null=True) 
    r3_user_rating = models.DecimalField(max_digits=10, decimal_places=1, default=None, blank=True, null=True)
    r3_cuisines = models.CharField(max_length=150, default=None, blank=True, null=True)
    r3_has_online_delivery = models.IntegerField(default=None, blank=True, null=True)

    r4_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    r4_price_range =  models.IntegerField(default=None, blank=True, null=True)
    r4_latitude =  models.CharField(max_length=50, default=None, blank=True, null=True)
    r4_longitude = models.CharField(max_length=50, default=None, blank=True, null=True)
    r4_photos_url = models.CharField(max_length=150, default=None, blank=True, null=True) 
    r4_user_rating = models.DecimalField(max_digits=10, decimal_places=1, default=None, blank=True, null=True)
    r4_cuisines = models.CharField(max_length=150, default=None, blank=True, null=True)
    r4_has_online_delivery = models.IntegerField(default=None, blank=True, null=True)


    # r1 = models.ForeignKey(Restaurants, related_name='Restaurant1', on_delete=models.CASCADE)
    # r2 = models.ForeignKey(Restaurants, related_name='Restaurant2', on_delete=models.CASCADE)
    # r3 = models.ForeignKey(Restaurants, related_name='Restaurant3', on_delete=models.CASCADE)
    # r4 = models.ForeignKey(Restaurants, related_name='Restaurant4', on_delete=models.CASCADE)
