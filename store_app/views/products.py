
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
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

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductSerializer
        return ProductCreateUpdateSerializer

