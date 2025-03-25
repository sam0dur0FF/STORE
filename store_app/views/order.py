from rest_framework import viewsets
from store_app.models import OrderItem
from store_app.serializers import OrderSerializer, OrderCreateUpdateSerializer



class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrderSerializer
        return OrderCreateUpdateSerializer