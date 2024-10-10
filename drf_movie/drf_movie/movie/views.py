# 从Django中导入render函数
from django.shortcuts import render
# 从Django中导入JsonResponse类
from django.http import JsonResponse,Http404
# 从rest_framework.decorators模块中导入@api_view装饰器
from rest_framework.decorators import api_view
# 从rest_framework模块中导入status常量和Response类
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from utils.permissions import IsAdminUserOrReadOnly

# 从当前目录下导入Movie模型和MovieListSerializer序列化器
from movie.models import Movie,Category
from movie.serializers import MovieSerializer,CategorySerializer
from utils.error import MovieError,UserError


class MovieFilter(filters.FilterSet):
    movie_name=filters.CharFilter(lookup_expr='icontains')
    category_id = filters.NumberFilter()
    region = filters.NumberFilter()

    class Meta:
        model=Movie
        fields = ['movie_name','category_id','region']


# 创建filter过滤器，用于搜索电影名称
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class=MovieFilter
    permission_classes = [IsAdminUserOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
