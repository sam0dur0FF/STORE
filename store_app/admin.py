from django.contrib import admin
from store_app.models import Category, Supplier, Address, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    ordering = (
        'name',
    )
    list_display = (
        'name',
        'contact_email',
        'phone_number',
    )
    search_fields = (
        'name',
        'contact_email',
        'phone_number',
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'country',
        'city',
        'street',
        'house',
    )
    search_fields = (
        'country',
        'city',
        'street',
        'house',
    )
    ordering = (
        'country',
        'city',
        'street',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order_date',
        'customer',
    )
    search_fields = (
        'customer__first_name',
        'customer__last_name',
        'customer__email',
    )
    ordering = (
        '-order_date',
    )
