from django.contrib import admin
from store_app.models import Category, Customer


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

# Зарегистрируйте модель Customer в админке с использованием декоратора @admin.register.
# Создайте класс CustomerAdmin, чтобы настроить отображение модели в админке:
# Установите отображение полей first_name, last_name, email, phone_number, date_joined, deleted в списке записей.
# Добавьте возможность поиска по полям first_name, last_name, email, phone_number.
# Установите сортировку записей по полю date_joined в порядке от самых новых записей к самым старым.
# Добавьте фильтрацию записей по полю deleted.Сделайте поле deleted редактируемым прямо в списке записей.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'date_joined', 'deleted')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    ordering = ['-date_joined']
    list_filter = ('deleted',)
    list_editable = ('deleted',)




