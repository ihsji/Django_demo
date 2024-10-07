# 导入 Django 中的管理模块、路径模块和包含默认路由器的 REST Framework 模块
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movie import views

# 创建默认路由器对象
router = DefaultRouter()
# 注册 movie 视图集到路由器中，并指定路径前缀为 'movie'
router.register(r'movie', views.MovieViewSet)
router.register(r'category',views.CategoryViewSet)

# 定义 URL 路由列表
urlpatterns = [
    # 设置 admin 管理路径
    path('admin/', admin.site.urls),
    # 设置 API 路径，包括注册的视图集路由
    path('api/', include(router.urls)),
    path('api/',include('djoser.urls')), 
    path('api/', include('djoser.urls.jwt')),
    # path('no_drf/',include('no_drf.urls',namespace='no_drf'))
]