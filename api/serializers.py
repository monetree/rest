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

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
