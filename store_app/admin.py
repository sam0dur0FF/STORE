from django.contrib import admin
from store_app.models import Category, Supplier, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

