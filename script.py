import os
from mailcap import lookup

import django
from django.db.models import Avg, F, Sum, Count

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'STORE.settings')
django.setup()

from store_app.models import *

# products = Product.objects.aggregate(amount = Sum(F("quantity") * F("price")))
# print(products)
#
# # product_agregate = Product.objects.aggregate(avg=Avg('price'))
# # print(product_agregate)



# Вычислить количество заказов и общую стоимость заказов для каждого клиента.
count_orders = Order.objects.values("customer__first_name", "customer__last_name").annotate(count= Count("id"),
total=Sum(F("items__quantity") * F("items__product__price"))
)

for order in count_orders:
    print(order)
