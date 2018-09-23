
from rest_framework import serializers
from .models import *
from django.db.models import Sum,Avg,Max,Min,Count,F,Q


#HyperlinkedModelSerializer
#ModelSerializer

class CatalogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catalog
        fields = ('id','name','no_of_pcs','per_piece_price','catalog')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'



# class CatalogData(serializers.ModelSerializer):
#     class Meta:
#         model = Catalog
#         fields = ('name', 'no_of_pcs', 'per_piece_price')


class CompanySerializer(serializers.ModelSerializer):
    # catalog_details = serializers.SerializerMethodField()
    user = serializers.StringRelatedField()
    catalog = serializers.StringRelatedField()

    class Meta:
        model = Company
        fields = '__all__'

    # def get_catalog_details(self, obj):
    #     company_id=Company.objects.values('id')
    #     # id=company_id['id']
    #     print(company_id)
    #     catalogdetails = Catalog.objects.values('per_piece_price','no_of_pcs','name')
    #     return catalogdetails
