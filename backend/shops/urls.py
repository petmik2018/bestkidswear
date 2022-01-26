from django.urls import path

from . import views

urlpatterns = [
    path('shops/', views.ShopsList.as_view()),
    ]