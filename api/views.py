 
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
