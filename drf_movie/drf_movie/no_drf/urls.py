# 从Django中导入路径函数和views模块
from django.urls import path
from no_drf import views

# 设置应用程序名称
app_name = 'no_drf'

# 定义URL模式列表
# 定义URL模式列表
urlpatterns = [
    # 对根路径的视图MovieList进行映射，并命名为'list'
    path('', views.MovieList, name='list'),
]