from django.db import models


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, related_name='orders')

    def __str__(self):
        return f"{self.id} by {self.customer}"

    class Meta:
        ordering = ['-order_date']
        get_latest_by = ['order_date']
