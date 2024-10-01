from django.contrib import admin
from movie.models import Movie, Category

# 注册电影模型类
admin.site.register(Movie)
# 注册分类模型类
admin.site.register(Category)
