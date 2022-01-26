from django.urls import path

from . import views

urlpatterns = [
    path('orders/', views.OrdersList.as_view()),
    path('orders/<pk>/', views.OrderDetail.as_view()),
    path('create_order/', views.CreateOrder.as_view()),
    path('order_item/<pk>/', views.OrderItemDetail.as_view()),
    path('order_items/', views.OrderItemsList.as_view()),
    path('user_orders/<slug:user_name>/', views.UserOrdersList.as_view()),
]