from django.db import models
from django.conf import settings
import uuid


class Category(models.Model):
    '''product categories'''
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=50,unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    '''all products'''
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

