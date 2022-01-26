from rest_framework import serializers
from .models import Information, Message


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = (
            "name",
            "content",
        )


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            "user",
            "subject",
            "content",
        )