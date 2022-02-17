from rest_framework.views import APIView

from .models import BrandClick
from rest_framework.response import Response

from .serializers import BrandClickSerializer


class ClicksList(APIView):

    def get(self, request, format=None):
        clicks = BrandClick.objects.all()
        serializer = BrandClickSerializer(clicks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BrandClickSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("wrong parameters")


# class CreateBrandClick(APIView):
#     def get(self, request, format=None):
#         orders = BrandClick.objects.all()
#         serializer = CreateBrandClickSerializer(orders, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = CreateBrandClickSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response("wrong parameters")
