from rest_framework import viewsets
from store_app.models import Supplier
from store_app.serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer



