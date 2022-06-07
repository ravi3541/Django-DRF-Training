from email.mime import base
from django.contrib import admin
from django.db import router
from django.urls import path,include

from rest_framework.routers import DefaultRouter
from productApi.views import CustomerViewSet, ProductViewSet

router = DefaultRouter()
router.register('product',ProductViewSet, basename='product')
router.register('customer',CustomerViewSet, basename='customer')


urlpatterns = [
    path('api/studentApi/',include('studentApi.urls')),
    path('api/empApi/',include('employeeApi.urls')),
    path('api/songsApi/',include('songsalbumApi.urls')),
    path('admin/', admin.site.urls),
    
    path('api/productApi/',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]
