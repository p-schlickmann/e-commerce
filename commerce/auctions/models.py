from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    img_url = models.CharField(max_length=2048)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    created_on = models.DateTimeField()

    def __str__(self):
        return f"{self.category} | {self.title} | {self.price}"


class Bid(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='bids')
    amount = models.IntegerField()
    created_on = models.DateTimeField()

    def __str__(self):
        return f"{self.item} | Bid: {self.amount}"
