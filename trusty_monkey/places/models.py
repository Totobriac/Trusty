from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from datetime import datetime    
        
        
class Restaurant(models.Model):
    maps = models.CharField(primary_key=True, max_length=140, unique=True)
    name = models.CharField(max_length=140)
    opened = ArrayField(models.CharField(max_length=1200, null=True, blank=True))
    website = models.CharField(max_length=800, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    restLat = models.FloatField()
    restLng = models.FloatField()
    adress = models.CharField(max_length=140, null=True, blank=True)
    def __str__(self):
        return self.name


class RestaurantReview(models.Model):    
    review_author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE)    
    maps = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):        
        return str(self.id)


class StarterPic(models.Model):
    restaurant_review = models.ForeignKey(RestaurantReview,
                                               on_delete=models.CASCADE)
    name_1 = models.CharField(max_length=40, null=True, blank=True)    
    picture_1 = models.ImageField()    
    
   
    class Meta: 
        verbose_name = 'StarterPics'
        verbose_name_plural = 'StarterPics'


class MainPic(models.Model):
    restaurant_review = models.ForeignKey(RestaurantReview,
                                               on_delete=models.CASCADE)       
    picture_1 = models.ImageField()   
   
    class Meta: 
        verbose_name = 'MainPics'
        verbose_name_plural = 'MainPics'

class DessertPic(models.Model):
    restaurant_review = models.ForeignKey(RestaurantReview,
                                                on_delete=models.CASCADE)       
    picture_1 = models.ImageField()      

    class Meta: 
        verbose_name = 'DessertPics'
        verbose_name_plural = 'DessertPics'


class MenuPic(models.Model):
    restaurant_review = models.ForeignKey(RestaurantReview,
                                                on_delete=models.CASCADE)
    picture_1 = models.ImageField()   
   
    class Meta: 
        verbose_name = 'MenuPics'
        verbose_name_plural = 'MenuPics'


class OutsidePic(models.Model):
    restaurant_review = models.ForeignKey(RestaurantReview,
                                                on_delete=models.CASCADE)
    picture_1 = models.ImageField()  

    class Meta: 
        verbose_name = 'OutsidePics'
        verbose_name_plural = 'OutsidePics'


class InsidePic(models.Model):
    restaurant_review = models.ForeignKey(RestaurantReview,
                                                on_delete=models.CASCADE)
    picture_1 = models.ImageField()    

    class Meta: 
        verbose_name = 'InsidePics'
        verbose_name_plural = 'InsidePics'