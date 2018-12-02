
# Create your views here.
from rest_framework.generics import ListAPIView
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
from rest_framework import mixins, filters
# from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Goods
from .serializer import GoodSerializer
from .filters import GoodsFilter


# class GoodsListView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         serializer = GoodSerializer(goods, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = GoodSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 1000

# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):


class GoodsListView(ListAPIView):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodSerializer
    pagination_class = StandardResultsSetPagination


    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)


class GoodslistViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页，分页，搜索，过滤，排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_fields = ('name', 'shop_price')
    filter_class = GoodsFilter
    search_fields = ('^name', 'goods_brief', 'category__name')
    ordering_fields = ('shop_price', 'add_time')

    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get('price_min', 0)
    #     if price_min:
    #         queryset = queryset.filter(shop_price__gt=int(price_min))
    #     return queryset

