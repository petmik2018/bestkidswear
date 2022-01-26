from django.urls import path

from . import views

urlpatterns = [
    path('stock/<pk>/', views.StockDetailsById.as_view()),
]