from rest_framework.views import APIView
from rest_framework.response import Response

from .models import New
from .serializers import NewShortSerializer


class NewsList(APIView):
    def get(self, request, format=None):
        news = New.objects.all()
        serializer = NewShortSerializer(news, many=True)
        return Response(serializer.data)

