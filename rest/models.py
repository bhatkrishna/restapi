from django.db import models
class Students(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    address = models.CharField(max_length=100)
# Create your models here.
