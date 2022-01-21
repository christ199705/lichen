from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
import json


# Create your views here.


def cuisine_all(request):
    if request.method == "GET":
        style_list = []
        for item in Style.objects.all():
            style_id = item.id
            style_name = item.style_name
            sql = "select id,count(*) as count from menu_dishes where Style_id = {}; ".format(style_id)
            for item2 in Dishes.objects.raw(sql):
                style_count = item2.count
            dict01 = {"id": style_id, "style_name": style_name, "style_count": style_count}
            style_list.append(dict01)
        return JsonResponse(style_list, safe=False, status=200)
    else:
        return JsonResponse({"error_code": "405",
                             "error_message": "You have to use the GET method"}, status=405)


def cuisine(request, sid):
    if request.method == 'GET':
        dishes_list = []
        data = Dishes.objects.filter(Style_id=sid)
        if len(data) == 0:
            return JsonResponse({})
        for item in data:
            dict01 = {"id": item.id, "dishes_name": item.dishes_name, "comment": item.comment,
                      "img_link": str(item.img_link), "stock": item.stock, "price": item.price, "volume": item.volume}
            dishes_list.append(dict01)
        return JsonResponse(dishes_list, safe=False, status=200)
    else:
        return JsonResponse({"error_code": "405",
                             "error_message": "You have to use the GET method"}, status=405)


def put_increment(request):
    if request.method == "PUT":
        json_data = json.loads(request.body)
        try:
            pid = int(json_data["pid"])
            type = int(json_data["type"])
        except KeyError:
            return JsonResponse({"error_code": 10000002,
                                 "error_message": "请求字段错误"},status=422)
        except ValueError:
            return JsonResponse({"error_code": 10000003,
                                 "error_message": "pid,type必须是数字"},status=422)
        if type == 0:
            dishes = Dishes.objects.get(id=pid)
            if dishes.stock == 0:
                return JsonResponse({"error_code": 10000001,
                                     "error_message": "库存已经为0"},status=422)
            dishes.stock -= 1
            dishes.save()
            return JsonResponse({"status_code": 200,
                                 "message": "修改库存成功"}, status=200)
        elif type == 1:
            dishes = Dishes.objects.get(id=pid)
            dishes.stock += 1
            dishes.save()
            return JsonResponse({"status_code": 200,
                                 "message": "修改库存成功"}, status=200)
        else:
            return JsonResponse({"error_code": 10000004,
                                 "error_message": "type 必须是 0 或者 1 !"}, status=422)
    else:
        return JsonResponse({"error_code": 405,
                             "error_message": "You have to use the PUT method"}, status=405)
