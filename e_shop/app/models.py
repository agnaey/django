from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class product (models.Model):
    pro_id=models.TextField()
    name=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ForeignKey(product,on_delete=models.CASCADE)

class Buy(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ForeignKey(product,on_delete=models.CASCADE)  
    price=models.IntegerField()             ##price is added bcs it should not change when product price incres after buying
    date=models.DateField(auto_now_add=True)
    
