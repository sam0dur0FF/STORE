
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from store_app.models import Product
from store_app.serializers import ProductSerializer, ProductCreateUpdateSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter]

    filterset_fields = [
        'price',
        'category',
    ]
    search_fields = [
        'price',
        'category',
    ]
    ordering_fields = [
        'price',
        'category',
        'name',
        'quantity'
    ]

    permission_classes = [
        IsAuthenticated

    ]

    authentication_classes = [
        BasicAuthentication

    ]




    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductSerializer
        return ProductCreateUpdateSerializer

