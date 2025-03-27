from store_app import models, serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class AddressView(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]