from rest_framework import serializers
from .models import Order, OrderDetail, Food


class FoodSerializer(serializers.ModelSerializer):
    ''' Food Serializer '''
    unit_price = serializers.FloatField(source='price')

    class Meta:
        model = Food
        fields = ['id', 'name', 'food_type','price','unit_price']


class OrderDetailSerializer(serializers.ModelSerializer):
    ''' Order Detail Serializer '''
    class Meta:
        model = OrderDetail
        fields = ['id', 'order', 'food', 'quantity','unit_price','line_total',]


class OrderSerializer(serializers.ModelSerializer):
    ''' Order Serializer '''
    order_detail = OrderDetailSerializer(many=True, read_only=False)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total', 'created', 'order_detail']
