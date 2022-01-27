from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Type, Action, Brand, Product
from .serializers import TypeSerializer, ActionDetailSerializer, ActionShortSerializer, ProductSerializer
from .serializers import BrandSerializer, BrandShortSerializer, ProductsListSerializer


class ActionsList(APIView):
    def get(self, request, format=None):
        actions = Action.objects.all()
        # serializer = ActionSerializer(actions, many=True)
        serializer = ActionShortSerializer(actions, many=True)
        return Response(serializer.data)


class BrandsList(APIView):
    def get(self, request, format=None):
        brands = Brand.objects.all()
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


class ProductsList(APIView):
    def get_object(self, brand_slug):
        try:
            return Brand.objects.get(slug=brand_slug)
        except Action.DoesNotExist:
            raise Http404

    def get(self, request, brand_slug, format=None):
        brand = self.get_object(brand_slug)
        serializer = ProductsListSerializer(brand)
        return Response(serializer.data)


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


# class ProductViewSet(viewsets.ModelViewSet):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()

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


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})

