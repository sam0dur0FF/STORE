from django.db import models



class OrderItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='orders')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.product.name}: {self.quantity} x {self.price}'