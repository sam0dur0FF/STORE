from django.contrib import admin
from store_app.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

