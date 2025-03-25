import os

import django
from datetime import datetime, timedelta
from django.db.models import Q, Max, Min, Count, OuterRef, Subquery, Avg, F, Value, Sum
import pandas as pd
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractIsoYear, ExtractMinute, Concat
from django.utils import timezone
from django.utils.dateparse import parse_datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'STORE.settings')
django.setup()
from store_app.models import *

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.expand_frame_repr", False)



def show_df(query_set):
    df = pd.DataFrame(query_set)
    print(df)

# a = Product.objects.values()
# show_df(a)

# b = Product.objects.aggregate(Avg('price'))
# print(b)
# print(*dir(Product.objects), sep='\n')
#
# bablo = Product.objects.annotate(total_qty = F('price') * F('quantity')).order_by('id')
# show_df(bablo.values())

# show_df(Product.objects.values('category__name').annotate(Avg('price')).order_by('price__avg'))


# price_range = Product.objects.aggregate(min_price = Min('price'), max_price = Max('price'))
# print(price_range)

# Вычислить количество заказов и общую стоимость заказов для каждого клиента.

# show_df((Order.objects.
#      values('customer').
#      annotate(orders_qty = Count('customer')).
#      annotate(
#         full_name=Concat(
#             F('customer__first_name'),
#             Value(' '),
#             F('customer__last_name')),
#         total_price = Sum(F('items__quantity') * F('items__price')),
#
#         ).
#      values('full_name', 'orders_qty', 'total_price')).
#      order_by('-orders_qty'))


# Рассчитать общий вес всех продуктов для каждой категории.
# k = ProductDetail.objects.values('product__category').annotate(
#     total_weight = Sum(F('weight') * F('product__quantity'))
#     ).values('product__category__name', 'total_weight').order_by('total_weight')
#
# show_df(k)


# show_df(
#     Product.objects.values('category__name').annotate(
#         total_weight = Sum(F('details__weight') * F('quantity'))).
#     annotate(category = F('category__name')).
#     values('category', 'total_weight').order_by('total_weight')
# )


# Вычислить количество различных продуктов, которые поставляет каждый поставщик.

show_df(
    Product.objects.values('supplier__name').
    annotate(product_qty = Count('id')).
    annotate(supplier = F('supplier__name')).
    values('supplier', 'product_qty').
    order_by('-product_qty')
)

# Вычислить среднюю продолжительность жизни продуктов
# (в днях) на основе даты производства и срока годности

show_df(
    ProductDetail.objects.annotate(
        live = F('expiration_date') - F('manufacturing_date')
    ).values()
)




