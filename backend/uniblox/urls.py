from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.views import ProductViewSet, CartViewSet, AdminViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'admin', AdminViewSet, basename='admin')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] 