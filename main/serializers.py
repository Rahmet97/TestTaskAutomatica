from rest_framework import serializers

from .models import ShoppingCenter, Visit


class ShoppingCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCenter
        fields = ['id', 'name']


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'date']
