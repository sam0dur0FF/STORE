from rest_framework import status, viewsets, mixins
from store_app.models import ProductDetail
from store_app.serializers import ProductDetailSerializer, ProductDetailCreateUpdateSerializer


class ProductDetailView(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()


    def get_serializer_class(self):
        if self.request.method in ('GET', 'PUT', 'PATCH'):
            return ProductDetailCreateUpdateSerializer
        return ProductDetailSerializer