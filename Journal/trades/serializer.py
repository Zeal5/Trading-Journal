
from rest_framework import serializers
from .models import Trades

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trades
        fields = '__all__'
