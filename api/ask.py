here is my models.py


    from __future__ import unicode_literals
    from django.db import models

    class User(models.Model):
        name = models.CharField(max_length=200)
        company_name = models.ForeignKey('Company',on_delete=models.CASCADE)

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
        company_name = models.ForeignKey(Company,on_delete=models.CASCADE)

        def __str__(self):
            return self.name



here is my seralizers.py

    from rest_framework import serializers
    from .models import *
    from django.db.models import Sum,Avg,Max,Min,Count,F,Q

    class CatalogSerializer(serializers.HyperlinkedModelSerializer):
        dynamic_data = serializers.SerializerMethodField()
        class Meta:
            model = Catalog
            fields = '__all__'

        def get_dynamic_data(self, obj):
            totalpieces = Catalog.objects.all().aggregate(total_pieces=Count('no_of_pcs'))
            totalprice = Catalog.objects.all().aggregate(total_price=Sum('per_piece_price'))
            return totalprice,totalpieces

    class CompanySerializer(serializers.ModelSerializer):
        class Meta:
            model = Company
            fields = ('name', 'phone_number', 'catalog','user')

    class UserSerializer(serializers.ModelSerializer):
        name = serializers.StringRelatedField()
        company_name = serializers.StringRelatedField()
        class Meta:
            model = User
            fields = '__all__'



here is my view.py

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

    class CompanyView(viewsets.ModelViewSet):
        queryset =  Company.objects.all()
        serializer_class = CompanySerializer

    class UserView(viewsets.ModelViewSet):
        queryset =  User.objects.all()
        serializer_class = UserSerializer



here is my urls.py


    from django.conf.urls import url, include
    from django.contrib import admin

    from api import views
    from rest_framework.urlpatterns import format_suffix_patterns
    from rest_framework import routers

    router = routers.DefaultRouter()
    router.register('catalogs',views.CatalogView)
    router.register('companies',views.CompanyView)
    router.register('users',views.UserView)

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'', include(router.urls)),
    ]





 when i will go
 http://127.0.0.1:8000/companies/

 m getting



         [
            {
                "name": "google",
                "phone_number": 12,
                "catalog": [
                    5
                ],
            }
        ]



m expecting this..

         [
            {
                "url": "google",
                "name": "google",
                "phone_number": 123214214,
                "catalog_details":[
                    "name": "sobhagya",
                    "no_of_pcs": 22,
                    "per_piece_price": "3567.00",
                ]
            }
        ]



here I am able to get only id of related_name which i have set as foreignkKey
but i am expection all the fields like this above..
