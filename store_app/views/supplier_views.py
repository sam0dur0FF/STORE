from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from store_app.models import Supplier
from store_app.serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAdminUser]



