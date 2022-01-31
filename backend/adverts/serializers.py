from rest_framework import serializers
from .models import Advert


class AdvertShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = (
            "id",
            "name",
            "main_image",
            "get_image",
            "get_absolute_url",
            "detailed_info",
            "date"
        )