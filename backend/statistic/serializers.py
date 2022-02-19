from rest_framework import serializers

from .models import AbstractClick


class ClickSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbstractClick
        fields = (
            "id",
            "brand",
            "product",
            "shop",
            "get_brand_name",
            "get_product_name",
            "get_shop_name",
            "get_date_time",
        )


class ClickAbstractSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbstractClick
        fields = (
            "id",
            "get_date_time"
        )
