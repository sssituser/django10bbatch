from django.db import models

# Create your models here.

class Customer(models.Model):
    CustomerId = models.IntegerField(primary_key=True)
    CustomerName = models.CharField(max_length=40)
    CustomerContact = models.CharField(max_length=20)
