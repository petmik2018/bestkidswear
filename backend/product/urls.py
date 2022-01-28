from django.urls import path

from . import views

urlpatterns = [
    path('brands/', views.BrandsList.as_view()),
    path('brands/<slug:brand_slug>/', views.BrandDetail.as_view()),
    path('products/search/', views.search),
    # path('products/<slug:action_slug>/', views.ActionDetail.as_view()),
    # path('products/<slug:brand_slug>/', views.ProductsList.as_view()),
    path('products/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('product/<pk>/', views.ProductDetailsById.as_view()),
]