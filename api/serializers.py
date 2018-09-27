from rest_framework import serializers
from .models import *
from django.db.models import Sum,Count


#HyperlinkedModelSerializer
#ModelSerializer
class UserSerializer(serializers.ModelSerializer):
    # name = serializers.StringRelatedField()
    # company_name = serializers.CharField()
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(UserSerializer, self).to_representation(instance)
        rep['company_name'] = instance.company_name.name
        return rep

class CatalogData(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ('name', 'no_of_pcs', 'per_piece_price')


class CompanySerializer(serializers.ModelSerializer):
    # catalog_details = serializers.SerializerMethodField()
    # name = serializers.StringRelatedField()

    # catalog = CatalogData(many=True)
    # user    = UserSerializer(many=True)

    class Meta:
        model = Company
        fields = ('name', 'phone_number', 'catalog','user')
        depth = 1

class CatalogSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = '__all__'




class CatalogSerializer(serializers.ModelSerializer):
    # company_details = CompanyData(many=True)
    total_pieces = serializers.SerializerMethodField()
    total_price  = serializers.SerializerMethodField()
    # company = CompanySerializer(source='company_name', read_only=True)
    # company_name = serializers.CharField()

    class Meta:
        model = Catalog
        fields = ('name','no_of_pcs','per_piece_price','company_name','total_pieces','total_price')
        depth = 1


    # def to_representation(self, instance):
    #     rep = super(CatalogSerializer, self).to_representation(instance)
    #     rep['company'] = {
    #                           "company_name":instance.company_name.name,
    #                           "phone_number":instance.company_name.phone_number,
    #                           "company_id":instance.company_name.id
    #                      }
    #     # rep['phone_number'] = instance.company_name.phone_number
    #     return rep

    # def company_details(self, instance):
    #     rep = super(CatalogSerializer, self).to_representation(instance)
    #     rep['company'] = {
    #                           "company_name":instance.company_name.name,
    #                           "phone_number":instance.company_name.phone_number,
    #                           "company_id":instance.company_name.id
    #                      }
    #     return rep

    def get_total_pieces(self, obj):
        totalpieces = Catalog.objects.aggregate(total_pieces=Count('no_of_pcs'))
        return totalpieces["total_pieces"]

    def get_total_price(self, obj):
        totalprice = Catalog.objects.aggregate(total_price=Sum('per_piece_price'))
        return totalprice["total_price"]



    # dynamic_data = serializers.SerializerMethodFieldcompany()
    # def get_dynamic_data(self, obj):
    #     totalpieces = Catalog.objects.all().aggregate(total_pieces=Count('no_of_pcs'))
    #     totalprice = Catalog.objects.all().aggregate(total_price=Sum('per_piece_price'))
    #     print(totalpieces["total_pieces"],totalprice["total_price"])
    #     return totalpieces["total_pieces"],totalprice["total_price"]
