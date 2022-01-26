from rest_framework import serializers
from .models import Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            "id",
            "name",
            "main_image",
            "get_image",
            "get_shop_url",
            "get_absolute_url",
        )