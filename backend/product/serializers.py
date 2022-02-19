from rest_framework import serializers
from .models import Brand, Product, Image
from stock.serializers import StockSerializer
from shops.serializers import WhereToBuySerializer
from statistic.serializers import ClickAbstractSerializer


class BrandShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "main_image",
            "get_image",
            "get_brand_url",
            "get_absolute_url",
            "is_active"
        )


class ClickProductSerializer(serializers.ModelSerializer):

    clicks = ClickAbstractSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "get_fullname",
            "clicks",
            "is_active"
        )


class BrandClicksSerializer(serializers.ModelSerializer):

    clicks = ClickAbstractSerializer(many=True)
    products = ClickProductSerializer(many=True)

    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "clicks",
            "products",
            "is_active"
        )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            "id",
            "get_image",
            "is_main",
        )


class ProductShortSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "get_absolute_url",
            "get_fullname",
            "images",
            "basic_price",
            "alt",
            "get_product_url",
            "is_active"
        )


class BrandSerializer(serializers.ModelSerializer):
    products = ProductShortSerializer(many=True)

    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "logo_image",
            "main_image",
            "short_info",
            "detailed_info",
            "get_logo",
            "get_image",
            "products"
        )


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    stocks = StockSerializer(many=True)
    brand = BrandShortSerializer(many=False)
    where_to_buy = WhereToBuySerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "brand",
            "get_absolute_url",
            "description",
            "basic_price",
            "get_fullname",
            "images",
            "stocks",
            "alt",
            "where_to_buy"
        )


class ProductsListSerializer(serializers.ModelSerializer):
    products = ProductShortSerializer(many=True)

    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
            "short_info",
            "get_image",
        )
