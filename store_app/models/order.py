from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='orders', null=True, blank=True)


    def __str__(self):
        return f"{self.id} by {self.user}"

    class Meta:
        ordering = ['-order_date']
        get_latest_by = ['order_date']
