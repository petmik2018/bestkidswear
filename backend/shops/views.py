from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404

from .models import Shop

from .serializers import ShopSerializer, ShopDetailSerializer


class ShopsList(APIView):
    def get(self, request, format=None):
        brands = Shop.objects.all()
        serializer = ShopSerializer(brands, many=True)
        return Response(serializer.data)


class ShopDetail(APIView):
    def get_object(self, shop_slug):
        try:
            return Shop.objects.get(slug=shop_slug)
        except Shop.DoesNotExist:
            raise Http404

    def get(self, request, shop_slug, format=None):
        shop = self.get_object(shop_slug)
        serializer = ShopDetailSerializer(shop)
        return Response(serializer.data)
