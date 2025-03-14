from rest_framework import viewsets
from store_app.models import OrderItem
from store_app.serializers import OrderItemSerializer, OrderItemCreateUpdateSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrderItemSerializer
        return OrderItemCreateUpdateSerializer