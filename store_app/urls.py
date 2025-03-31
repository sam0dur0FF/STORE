from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store_app.views.address import AddressView
from store_app.views.category import CategoryView
from store_app.views.customer_views import CustomerView
from store_app.views.order import OrderViewSet
from store_app.views.order_items import OrderItemViewSet
from store_app.views.product_detail_views import ProductDetailView
from store_app.views.products import ProductViewSet
from store_app.views.supplier_views import SupplierViewSet
from store_app.views.user_orders import UserOrdersViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'categories', CategoryView)
router.register(r'customers', CustomerView)
router.register(r'products', ProductViewSet)
router.register(r'products_details', ProductDetailView)
router.register(r'order_items', OrderItemViewSet)
router.register(r'addresses', AddressView)
router.register(r'orders', OrderViewSet)
router.register(r'suppliers', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('my_orders/', UserOrdersViewSet.as_view(), name="my_orders"),
    path('token-get/', TokenObtainPairView.as_view(), name='get_token'),
    path('token-update/', TokenRefreshView.as_view(), name='update_token'),
]

