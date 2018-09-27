from __future__ import unicode_literals
from django.http import HttpResponse
from .models import *
import json
from django.http import JsonResponse, HttpResponse
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view


# @api_view(['GET', 'POST'])
# def CatalogView(request):
#     if request.method == 'GET':
#         catalogs = Catalog.objects.select_related('company_name')
#         serializer = CatalogSerializer(catalogs, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = CatalogSerializerPost(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CatalogView(viewsets.ModelViewSet):
    queryset =  Catalog.objects.select_related('company_name')
    serializer_class = CatalogSerializerPost

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = CatalogSerializer
        return serializer_class


class CompanyView(viewsets.ModelViewSet):
    queryset =  Company.objects.all()
    serializer_class = CompanySerializer

class UserView(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UserSerializer
