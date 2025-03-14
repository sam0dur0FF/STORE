from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from store_app.models import Customer
from store_app.serializers import CustomerSerializer, CustomerCreateUpdateSerializer


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer
        return CustomerCreateUpdateSerializer
