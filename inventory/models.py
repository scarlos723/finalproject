from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Product(models.Model):
    name = models.CharField(max_length=192, null=True)
    model =  models.CharField(max_length=192, null=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    sold_number = models.IntegerField()
    

class Client(models.Model):
    name = models.CharField(max_length=192, null=True)
    lastname = models.CharField(max_length=192, null=True)
    tel =  models.IntegerField()
    id_number = models.IntegerField()


class Order(models.Model):
    kind = models.CharField(max_length=192, null=True)
    value = models.IntegerField()
    client = models.ForeignKey(Client, on_delete = models.CASCADE, related_name="order_client")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="order_user")
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = models.CharField(max_length=255, null=True)


