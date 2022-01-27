from django.urls import path

from . import views

urlpatterns = [
    path('shops/', views.ShopsList.as_view()),
    path('shops/<slug:shop_slug>/', views.ShopDetail.as_view()),
    ]