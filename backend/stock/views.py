from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Stock
from .serializers import StockSerializer


class StockDetailsById(APIView):
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stock = self.get_object(pk)
        serializer = StockSerializer(stock, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        model_object = self.get_object(pk)
        serializer = StockSerializer(model_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("wrong parameters")