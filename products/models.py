from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    