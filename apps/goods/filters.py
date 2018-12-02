__author__ = 'Harley'
__date__ = '2018-12-02 22:32'

from rest_framework import generics
import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品过滤类
    """
    min_price = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price', 'name']