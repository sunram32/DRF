from django.db import models

# Create your models here.
class TableB(models.Model):
    price_type = models.CharField(max_length=30)
    price_value = models.FloatField()

class TableA(models.Model):
    product = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    price_type = models.ForeignKey(TableB, on_delete=models.CASCADE)