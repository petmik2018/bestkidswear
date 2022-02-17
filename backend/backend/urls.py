from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('profiles.urls')),
    path('api/v1/', include('stock.urls')),
    path('api/v1/', include('contact.urls')),
    path('api/v1/', include('shops.urls')),
    path('api/v1/', include('adverts.urls')),
    path('api/v1/', include('statistic.urls')),
    # path('api/v1/', include('news.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
