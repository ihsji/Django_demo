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

# 从当前目录下导入Movie模型和MovieListSerializer序列化器
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer