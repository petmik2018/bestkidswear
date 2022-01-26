from django.http import Http404
from rest_framework import status
from django.http import JsonResponse

from rest_framework.views import APIView

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import BonusSettings, Profile
from .serializers import BonusSettingsSerializer, ProfileSerializer, PatchProfileSerializer


class GetBonusSettings(APIView):
    def get(self, request, format=None):
        bonus_settings = BonusSettings.objects.all()
        serializer = BonusSettingsSerializer(bonus_settings, many=True)
        return Response(serializer.data)


class ProfilesList(APIView):
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetail(APIView):

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class PatchProfileDetail(APIView):

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = PatchProfileSerializer(profile)
        return Response(serializer.data)

    def patch(self, request, pk):
        model_object = self.get_object(pk)
        serializer = PatchProfileSerializer(model_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("wrong parameters")



