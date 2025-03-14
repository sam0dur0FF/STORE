from django.urls import path, include
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'categories', )
router.register(r'suppliers', )
router.register(r'products', )

urlpatterns = [
    path('', include(router.urls)),
]
