from django.urls import path

from . import views

urlpatterns = [
    path('clicks/', views.ClicksList.as_view()),
]