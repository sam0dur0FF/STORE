from store_app import models, serializers
from rest_framework import viewsets


class CategoryView(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer



