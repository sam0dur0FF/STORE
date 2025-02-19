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


class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField()
    street = models.CharField()
    house = models.CharField()

    def __str__(self):
        return f"{self.street}, {self.house}"

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, related_name='orders')

    def __str__(self):
        return f"{self.id} by {self.customer}"

    class Meta:
        ordering = ['-order_date']
        get_latest_by = ['order_date']

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
