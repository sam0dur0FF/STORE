from django.contrib import admin
from store_app.models import Category, Supplier, Address, Order, Customer



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'date_joined', 'deleted')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    ordering = ['-date_joined']
    list_filter = ('deleted',)
    list_editable = ('deleted',)



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
