from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from stock.models import Stock

from .serializers import OrderSerializer, CreateOrderSerializer, CreateOrderTestSerializer, OrderItemSerializer


class OrdersList(APIView):

    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("wrong parameters")


class OrderDetail(APIView):

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class CreateOrder(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = CreateOrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("wrong parameters")


class OrderItemsList(APIView):

    def get(self, request, format=None):
        items = OrderItem.objects.all()
        serializer = OrderItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        item = request.data
        serializer = OrderItemSerializer(data=item)
        product_id = item['product_id']
        size = item['size']
        quantity = item['quantity']
        stock = Stock.objects.all().filter(product=product_id ).filter(size=size)[0]
        stock.quantity -= quantity
        stock.save()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("wrong parameters")


class OrderItemDetail(APIView):

    def get_object(self, pk):
        try:
            return OrderItem.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = OrderItemSerializer(item)
        return Response(serializer.data)


class CreateOrderTest(APIView):

    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = CreateOrderTestSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateOrderTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("wrong parameters")


class UserOrdersList(APIView):
    def get(self, request, user_name, format=None):
        orders = Order.objects.all().filter(user__username=user_name)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)