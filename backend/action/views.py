from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Type, Action
from .serializers import ActionDetailSerializer, ActionShortSerializer


class ActionsList(APIView):
    def get(self, request, format=None):
        actions = Action.objects.all()
        # serializer = ActionSerializer(actions, many=True)
        serializer = ActionShortSerializer(actions, many=True)
        return Response(serializer.data)


class ActionDetail(APIView):
    def get_object(self, action_slug):
        try:
            return Action.objects.get(slug=action_slug)
        except Action.DoesNotExist:
            raise Http404

    def get(self, request, action_slug, format=None):
        action = self.get_object(action_slug)
        serializer = ActionDetailSerializer(action)
        return Response(serializer.data)

class TypeDetail(APIView):
    def get_object(self, type_slug):
        try:
            return Type.objects.get(slug=type_slug)
        except Type.DoesNotExist:
            raise Http404

    def get(self, request, type_slug, format=None):
            type = self.get_object(type_slug)
            serializer = TypeSerializer(type)
            return Response(serializer.data)