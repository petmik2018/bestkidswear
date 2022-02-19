from rest_framework.views import APIView
from django.http import Http404

from rest_framework.response import Response

from .models import AbstractClick
from product.models import Brand

from .serializers import ClickSerializer


class ClicksList(APIView):

    def get(self, request, format=None):
        clicks = AbstractClick.objects.all()
        serializer = ClickSerializer(clicks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClickSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("wrong parameters")

class BrandClicksList(APIView):
    def get_objects(self, pk):
        try:
            return AbstractClick.objects.filter(brand=pk)
        except AbstractClick.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        click = self.get_objects(pk)
        serializer = ClickSerializer(click, many=True)
        return Response(serializer.data)


