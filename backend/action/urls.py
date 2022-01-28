from django.urls import path

from . import views

urlpatterns = [
    path('type/<slug:type_slug>/', views.TypeDetail.as_view()),
    path('actions/', views.ActionsList.as_view()),
]
