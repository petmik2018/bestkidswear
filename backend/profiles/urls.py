from django.urls import path

from . import views

urlpatterns = [
    path('profiles/', views.ProfilesList.as_view()),
    path('bonuses/', views.GetBonusSettings.as_view()),
    # path('profile/<pk>/', views.ProfileDetail.as_view()),
    path('profile/<slug:username>/', views.ProfileDetail.as_view()),
    path('patch_profile/<pk>/', views.PatchProfileDetail.as_view()),
]