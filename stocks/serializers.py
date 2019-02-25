from rest_framework import serializers
from .models import StockDetail

class StockDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockDetail
        fields = ['ticker','opens','closes','volume']
        
