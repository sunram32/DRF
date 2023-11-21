from main.models import *
from rest_framework import serializers

class TableASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TableA
        fields = ['id', 'product', 'category' , 'price_type']

class TableBSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TableB
        fields = ['id', 'price_type', 'price_value']