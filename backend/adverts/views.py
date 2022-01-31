from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Advert
from .serializers import AdvertShortSerializer


class AdvertsList(APIView):
    def get(self, request, format=None):
        news = Advert.objects.all()
        serializer = AdvertShortSerializer(news, many=True)
        return Response(serializer.data)
