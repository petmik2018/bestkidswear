from rest_framework import serializers
from .models import Type, Action, Brand, Product, Image
from stock.serializers import StockSerializer


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
            "alt"
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


class ActionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "get_image",
            "is_active",
            "get_brand_url"
        )


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    stocks = StockSerializer(many=True)
    brand = BrandShortSerializer(many=False)

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
            "alt"
        )


class ActionDetailSerializer(serializers.ModelSerializer):
    products = ProductShortSerializer(many=True)

    class Meta:
        model = Action
        fields = (
            "id",
            "name",
            "get_absolute_url",
            # "products",
            "short_info",
            "get_image",
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


class ActionSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Action
        fields = (
            "id",
            "name",
            "get_absolute_url",
            # 'products',
            "short_info",
            "get_image",
        )


class TypeSerializer(serializers.ModelSerializer):
    actions = ActionShortSerializer(many=True)

    class Meta:
        model = Type
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "actions"
        )
