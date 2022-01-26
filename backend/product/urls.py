from django.urls import path

from . import views

urlpatterns = [
    path('type/<slug:type_slug>/', views.TypeDetail.as_view()),
    path('actions/', views.ActionsList.as_view()),
    path('brands/<slug:brand_slug>/', views.BrandDetail.as_view()),
    path('products/search/', views.search),
    path('products/<slug:action_slug>/', views.ActionDetail.as_view()),
    path('products/<slug:action_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('product/<pk>/', views.ProductDetailsById.as_view()),
]