from django.db import models

# Create your models here.
class Producto(models.Model):
    name =  models.CharField(max_length=50)
    stock = models.IntegerField()
    price = models.IntegerField()
    paused = models.BooleanField(default=False)
