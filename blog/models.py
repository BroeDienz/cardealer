from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

# Create your models here.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    register = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    vin = models.CharField(max_length=100)  
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.make
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
class CartItem(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["model", "year", "price"]   
    