from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    