from .models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductDetail
        fields = '__all__'


class ProductDetailCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'first_name',
            'last_name',
            "email",
            'is_active',
        ]



class CustomerCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = [
            'date_joined',
            'deleted',
            'deleted_at',
        ]

    def validate_phone_number(self, value):
        if 10 <= len(value) <= 15 and value.isdigit():
            return value
        raise serializers.ValidationError('Phone number must be between 10 and 15 digits')


class OrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(read_only=True)
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    order = OrderSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def validate_quantity(self, value):
        if 0 < value <= 1000:
            return value
        raise serializers.ValidationError('Quantity must be between 0 and 100')
