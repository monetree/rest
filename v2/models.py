
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Catalog(models.Model):
    name = models.CharField(max_length=200)
    no_of_pcs = models.IntegerField(null=True,blank=True)
    per_piece_price = models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2)


    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    catalog = models.ForeignKey(Catalog,on_delete=models.CASCADE,related_name='catalog')

    def __str__(self):
        return self.name
