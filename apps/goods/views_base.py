__author__ = 'Harley'
__date__ = '2018-12-01 21:28'

from django.views.generic.base import View

from .models import Goods


class GoodListView(View):
    def get(self, request):
        good_list = []
        goods = Goods.objects.all()[:10]

        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     json_dict["desc"] = good.goods_desc
        #     good_list.append(json_dict)

        # from django.forms.models import model_to_dict
        # for good in goods:
        #     good_dict = model_to_dict(good)
        #     good_list.append(good_dict)

        # from django.http import HttpResponse
        # import json
        # return HttpResponse(json.dumps(good_list), content_type="application/json")

        from django.http import JsonResponse
        import json
        from django.core import serializers
        json_data = serializers.serialize("json", goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)
