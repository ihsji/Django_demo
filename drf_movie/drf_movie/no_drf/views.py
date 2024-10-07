from django.shortcuts import render
from django.http import JsonResponse

from movie.models import Movie,Category

def MovieList(request):
    # 获取所有电影数据
    movies = Movie.objects.all().values_list()
    # 将数据转换为列表形式
    data = {
      	'movie_name':'碟中谍',
      	'rate': 7.8
    }
    # 返回JSON响应
    return JsonResponse(data, safe=False)
