from django.db import models

class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.street}, {self.house}"

