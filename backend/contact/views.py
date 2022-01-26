from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from django.conf import settings
from django.core.mail import send_mail

from .models import Information, Message

from .serializers import InformationSerializer, MessageSerializer


class SendEmail(APIView):

    def get(self, request, email, order, format=None):
        subject = 'Заказ в магазине SuperZero'
        text = 'Здравствуйте, \r' \
               'Ваш заказ № ' + order + ' в магазине SuperZero сформирован.\r' \
               'Как только он будет готов к поставке, мы Вам сообщим.\r\r' \
               'С уважением, Магазин SuperZero\r' \
               'superzeroshop@yandex.ru\r' \
               '+7(916)350-3061'
        send_mail(subject, text, settings.EMAIL_HOST_USER, [email])
        print(settings.EMAIL_HOST_USER)
        print(email)
        text = 'Клиент сделал заказ № ' + order
        send_mail(subject, text, settings.EMAIL_HOST_USER, ['petmik@yandex.ru'])
        return Response('success')


class InformationList(APIView):

    def get(self, request, format=None):
        orders = Information.objects.all()
        serializer = InformationSerializer(orders, many=True)
        return Response(serializer.data)


class MessageList(APIView):

    def get(self, request, format=None):
        orders = Message.objects.all()
        serializer = MessageSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("wrong parameters")