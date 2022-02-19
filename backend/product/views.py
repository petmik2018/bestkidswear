from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Brand, Product
from .serializers import ProductSerializer, ProductsListSerializer
from .serializers import BrandSerializer, BrandShortSerializer


class BrandsList(APIView):
    def get(self, request, format=None):
        brands = Brand.objects.all().filter(is_active=True)
        serializer = BrandShortSerializer(brands, many=True)
        return Response(serializer.data)


class BrandDetail(APIView):
    def get_object(self, brand_slug):
        try:
            return Brand.objects.get(slug=brand_slug)
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, brand_slug, format=None):
        brand = self.get_object(brand_slug)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)


# class ProductsList(APIView):
#     def get_object(self, brand_slug):
#         try:
#             return Brand.objects.get(slug=brand_slug)
#         except Brand.DoesNotExist:
#             raise Http404
#
#     def get(self, request, brand_slug, format=None):
#         brand = self.get_object(brand_slug)
#         serializer = ProductsListSerializer(brand)
#         return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, product_slug):
        try:
            return Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, product_slug, format=None):
        product = self.get_object(product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductDetailsById(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})

