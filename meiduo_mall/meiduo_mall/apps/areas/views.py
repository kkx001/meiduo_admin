from django.shortcuts import render

# Create your views here.
from django.views import View
from django.core.cache import cache
from .models import Area
import logging
from django import http
from meiduo_mall.utils.response_code import RETCODE

# 日志
logger = logging.getLogger('django')


class AreasView(View):
    """省市区三级联动"""

    def get(self, request):
        # 判断当前查询的数据是省级还是市区的数据
        area_id = request.GET.get('area_id')

        if not area_id:
            # 获取并判断是否有缓存
            province_list = cache.get('province_list')

            if not province_list:
                # 查询省级数据
                try:

                    province_model_list = Area.objects.filter(parent__isnull=True)
                    # 需要将模型列表转化成字典列表
                    province_list = []
                    for province_model in province_model_list:
                        province_dict = {
                            "id": province_model.id,
                            "name": province_model.name
                        }
                        province_list.append(province_dict)
                    # 缓存省份字典列表数据：默认存储到'default'的配置中
                    cache.set('province_list', province_list, 3600)
                except Exception as e:
                    logger.error(e)
                    return http.JsonResponse({'code': RETCODE.DBERR, 'errmsg': '查询省份数据错误'})

            # 响应省级JSON
            return http.JsonResponse({'code': RETCODE.OK, 'errmsg': "OK", 'province_list': province_list})

        else:
            # 判断是否有缓存
            sub_data = cache.get('sub_area_' + area_id)

            if not sub_data:
                # 查询城市或县区数据
                try:
                    parent_model = Area.objects.get(id=area_id)
                    sub_model_list = parent_model.subs.all()

                    # 将子级模型列表转化为字典列表
                    subs = []
                    for sub_model in sub_model_list:
                        sub_dict = {
                            "id": sub_model.id,
                            "name": sub_model.name
                        }
                        subs.append(sub_dict)

                    # 构建子级json数据
                    sub_data = {
                        'id': parent_model.id,
                        'name': parent_model.name,
                        'subs': subs
                    }

                    # 缓存城市或县区
                    cache.set('sub_area_' + area_id, sub_data, 3600)

                except Exception as e:
                    logger.error(e)
                    return http.JsonResponse({'code': RETCODE.DBERR, 'errmsg': '查询城市或区县数据错误'})

            return http.JsonResponse({'code': RETCODE.OK, 'errmsg': "OK", 'sub_data': sub_data})
