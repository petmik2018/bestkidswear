from django.urls import path

from . import views

urlpatterns = [
    path('contact/<email>/<order>/', views.SendEmail.as_view()),
    path('information/', views.InformationList.as_view()),
    path('message/', views.MessageList.as_view()),
    ]