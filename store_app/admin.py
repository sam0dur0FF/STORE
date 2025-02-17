from django.contrib import admin
from store_app.models import Category, Supplier


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'contact_email', 'phone_number')
    search_fields = ('name', 'contact_email', 'phone_number')
