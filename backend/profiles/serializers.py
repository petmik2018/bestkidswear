from rest_framework import serializers

from .models import BonusSettings, Profile, User


class BonusSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonusSettings
        fields = (
            "initial_bonus",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "children"
        )


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username"
        )


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "name",
            "email",
            'phone',
            "address",
            "bonuses"
        )


class PatchProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            "id",
            "get_user_id",
            "name",
            "email",
            'phone',
            "address",
        )