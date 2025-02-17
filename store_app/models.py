from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'


class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ['name', 'contact_email']

    def __str__(self):
        return self.name


# Задание 2.3: Создание модели Product
# Создайте модель Product с полями:
# name (максимальная длина 100 символов).
# category (внешний ключ на модель Category с поведением PROTECT при удалении и с названием обратной связи products).
# supplier (внешний ключ на модель Supplier с поведением PROTECT при удалении и с названием обратной связи products).
# price (десятичное поле с максимумом 10 цифр и 2 десятичными знаками).
# quantity (положительное целое число).
# article (максимальная длина 100 символов, уникальное значение, имеет пояснение "Unique string product id" и индекс).
# available (логическое поле с значением по умолчанию True).
# Реализуйте метод __str__, чтобы он возвращал значение поля name.
# Добавьте мета-класс для модели:
# Установите сортировку по полям category и quantity в алфавитном порядке.

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='products')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField()
    article = models.CharField(max_length=100, unique=True, help_text="Unique string product id", db_index=True)
    available = models.BooleanField(default=True)


def __str__(self):
    return self.name

class Meta:
    ordering = ['category', "quantity"]