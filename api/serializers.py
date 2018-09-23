
from rest_framework import serializers
from .models import *
from django.db.models import Sum,Avg,Max,Min,Count,F,Q


#HyperlinkedModelSerializer
#ModelSerializer

class CatalogSerializer(serializers.HyperlinkedModelSerializer):
    dynamic_data = serializers.SerializerMethodField()
    class Meta:
        model = Catalog
        fields = '__all__'

    def get_dynamic_data(self, obj):
        totalpieces = Catalog.objects.all().aggregate(total_pieces=Count('no_of_pcs'))
        totalprice = Catalog.objects.all().aggregate(total_price=Sum('per_piece_price'))
        return totalprice,totalpieces


class UserSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    company_name = serializers.StringRelatedField()
    class Meta:
        model = User
        fields = '__all__'



class CatalogData(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ('name', 'no_of_pcs', 'per_piece_price')


class CompanySerializer(serializers.ModelSerializer):
    # catalog_details = serializers.SerializerMethodField()
    name = serializers.StringRelatedField()
    catalog = CatalogData(many=True)
    user = UserSerializer(many=True)
    class Meta:
        model = Company
        fields = ('name', 'phone_number', 'catalog','user')

    # def get_catalog_details(self, obj):
    #     company_id=Company.objects.values('id')
    #     # id=company_id['id']
    #     print(company_id)
    #     catalogdetails = Catalog.objects.values('per_piece_price','no_of_pcs','name')
    #     return catalogdetails
