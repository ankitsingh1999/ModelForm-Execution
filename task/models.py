from django.db import models


# Create your models here.

class Product(models.Model):
    Name = models.CharField(max_length=50)
    Email_id = models.EmailField()
    Phone_number = models.IntegerField(max_length=20)
    Image = models.ImageField()