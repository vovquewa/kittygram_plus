from django.urls import include, path
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet


router = DefaultRouter()
router.register('cats', CatViewSet, basename='cat')
router.register('owners', OwnerViewSet, basename='owner')
router.register(r'mycats', LightCatViewSet, basename='mycats')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]