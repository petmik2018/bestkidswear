from rest_framework import serializers
from .models import Shop, ShopBrand, WhereToBuy


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
            "main_link"
        )


class ShopBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopBrand
        fields = (
            "get_brand_name",
            "get_brand_url"
        )


class ShopDetailSerializer(serializers.ModelSerializer):
    brands = ShopBrandSerializer(many=True)

    class Meta:
        model = Shop
        fields = (
            "id",
            "name",
            "get_logo",
            "get_image",
            "get_shop_url",
            "get_absolute_url",
            "short_info",
            "detailed_info",
            "brands",
        )


class WhereToBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = WhereToBuy
        fields = (
            "shop",
            "link"
        )