from django.db import models

# Create your models here.

class student (models.Model):
    roll_no=models.IntegerField()
    name=models.TextField()
    age=models.IntegerField()
