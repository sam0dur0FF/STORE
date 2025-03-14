from rest_framework import viewsets
from store_app.models import Product
from store_app.serializers import ProductSerializer, ProductCreateUpdateSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductSerializer
        return ProductCreateUpdateSerializer
