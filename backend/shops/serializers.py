from rest_framework import serializers
from .models import Shop, ShopBrand
from product.serializers import BrandShortSerializer


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


class ShopBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopBrand
        fields = (
            "brand",
            "get_brand_name",
            "get_brand_link"
        )


class ShopDetailSerializer(serializers.ModelSerializer):
    brands = ShopBrandSerializer(many=True)

    class Meta:
        model = Shop
        fields = (
            "id",
            "name",
            "main_image",
            "get_image",
            "get_shop_url",
            "get_absolute_url",
            "brands",
        )
