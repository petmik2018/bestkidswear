from rest_framework import serializers
from .models import Type, Action


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


class ActionDetailSerializer(serializers.ModelSerializer):
    # products = ProductShortSerializer(many=True)

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


class ActionSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)

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
