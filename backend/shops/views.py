from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Shop

from .serializers import ShopSerializer


class ShopsList(APIView):
    def get(self, request, format=None):
        brands = Shop.objects.all()
        serializer = ShopSerializer(brands, many=True)
        return Response(serializer.data)
