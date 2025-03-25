from rest_framework import status, viewsets, mixins
from store_app.models import ProductDetail
from store_app.serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = SupplierSerializer



