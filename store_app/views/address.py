from store_app import models, serializers
from rest_framework import viewsets


class AddressView(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer