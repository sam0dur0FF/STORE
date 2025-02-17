from django.contrib import admin
from store_app.models import Category

# Задание 3.1: Настройка модели Category в админке
# Зарегистрируйте модель Category в админке с использованием декоратора @admin.register.
# Создайте класс CategoryAdmin, чтобы настроить отображение модели в админке:
# Установите отображение поля name в списке записей.
# Добавьте возможность поиска по полю name.
# Установите сортировку записей по полю name в алфавитном порядке.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

