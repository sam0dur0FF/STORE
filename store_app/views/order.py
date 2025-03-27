from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from store_app.models import Order
from store_app.serializers import OrderSerializer, OrderCreateUpdateSerializer



class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrderSerializer
        return OrderCreateUpdateSerializer