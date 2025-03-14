from django.urls import path, include
from rest_framework.routers import DefaultRouter

from store_app.views.address import AddressView
from store_app.views.category import CategoryView
from store_app.views.order_items import OrderItemViewSet
from store_app.views.product_detail_views import ProductDetailView
from store_app.views.products import ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryView)
# router.register(r'suppliers', )
router.register(r'products', ProductViewSet)
router.register(r'products_details', ProductDetailView)
router.register(r'order_items', OrderItemViewSet)
router.register(r'address', AddressView)

urlpatterns = [
    path('', include(router.urls)),
]
