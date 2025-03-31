from rest_framework import viewsets
from store_app.models import Order
from store_app.permissions import IsCustomerOrReadOnly, CanViewStatisticsPermission
from store_app.serializers import OrderSerializer, OrderCreateUpdateSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = (IsCustomerOrReadOnly,)


    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrderSerializer
        return OrderCreateUpdateSerializer


    @action(detail=False, methods=['get'], permission_classes=[CanViewStatisticsPermission])
    def statistics(self, request):
        stats = Order.objects.count()
        return Response(stats)
