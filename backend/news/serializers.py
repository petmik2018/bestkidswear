from rest_framework import serializers
from .models import New


class NewShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = (
            "id",
            "name",
            "main_image",
            "get_image",
            "get_absolute_url",
            "detailed_info",
            "date"
        )

