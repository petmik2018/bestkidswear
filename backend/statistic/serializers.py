from rest_framework import serializers

from .models import BrandClick


class BrandClickSerializer(serializers.ModelSerializer):

    class Meta:
        model = BrandClick
        fields = (
            "id",
            "brand",
            "get_brand_name",
            "get_date_time",
        )
