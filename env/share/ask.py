Here is my models.py



    from __future__ import unicode_literals
    from django.db import models

    class User(models.Model):
        name = models.CharField(max_length=200)
        company_name = models.ForeignKey('Company',on_delete=models.CASCADE,related_name='user')

        def __str__(self):
            return self.name

    class Company(models.Model):
        name = models.CharField(max_length=200)
        phone_number = models.IntegerField(null=True,blank=True)

        def __str__(self):
            return self.name

    class Catalog(models.Model):
        name = models.CharField(max_length=200)
        no_of_pcs = models.IntegerField(null=True,blank=True)
        per_piece_price = models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2)
        company_name = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='catalog')

        def __str__(self):
            return self.name


here is my serializers.py



    from rest_framework import serializers
    from .models import *
    from django.db.models import Sum,Count

    class CatalogSerializer(serializers.ModelSerializer):
        # company_details = CompanyData(many=True)
        total_pieces = serializers.SerializerMethodField()
        total_price = serializers.SerializerMethodField()
        # company = CompanySerializer(source='company_name')

        class Meta:
            model = Catalog
            fields = ('name','no_of_pcs','per_piece_price','company_name','total_pieces','total_price')
            depth = 1

        def get_total_pieces(self, obj):
            totalpieces = Catalog.objects.aggregate(total_pieces=Count('no_of_pcs'))
            return totalpieces["total_pieces"]

        def get_total_price(self, obj):
            totalprice = Catalog.objects.aggregate(total_price=Sum('per_piece_price'))
            return totalprice["total_price"]


        def to_representation(self, instance):
            rep = super(CatalogSerializer, self).to_representation(instance)
            rep['catalog'] = instance.name
            return rep


here is my views.py



    from __future__ import unicode_literals
    from django.http import HttpResponse
    from .models import *
    import json
    from django.http import JsonResponse, HttpResponse
    from .serializers import *
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework import status
    from rest_framework import viewsets

    class CatalogView(viewsets.ModelViewSet):
        queryset =  Catalog.objects.select_related('company_name')
        serializer_class = CatalogSerializer


please check the screen shot i have shared.
here no fields is coming for company.
i wants to post company along with all fields of catalog.

thanks..
