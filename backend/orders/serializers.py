from rest_framework import serializers
from .models import Order, OrderItem
from profiles.serializers import UserSerializer, UserShortSerializer


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "product",
            "size",
            "price",
            "quantity"
        )


class OrderSerializer(serializers.ModelSerializer):
    user = UserShortSerializer(many=False)
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "status",
            "get_data",
            "items"
        )


class CreateOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
        )


class CreateOrderTestSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "items"
        )


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "order",
            "product_id",
            "product",
            "size",
            "price",
            "quantity"
        )