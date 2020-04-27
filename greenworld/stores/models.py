from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField(max_length=None, blank=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    zipcode = models.IntegerField(max_length=6, default=000000)
    created_at = models.DateTimeField(auto_now_add=True)
    