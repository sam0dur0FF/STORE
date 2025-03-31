from django.db import models
from django.contrib.auth import get_user_model


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='orders', null=True, blank=True)



    def __str__(self):
        return f"{self.id} by {self.customer}"

    class Meta:
        ordering = ['-order_date']
        get_latest_by = ['order_date']
        permissions = [
            ("can_view_statistics", "Can view statistics"),
        ]
