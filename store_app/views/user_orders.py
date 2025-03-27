from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from store_app.models import Order
from store_app.serializers import OrderSerializer


class UserOrdersViewSet(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
