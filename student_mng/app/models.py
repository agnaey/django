from django.db import models

# Create your models here.
class Students(models.Model):
    roll_no=models.IntegerField()
    name=models.TextField()
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.IntegerField()
    
