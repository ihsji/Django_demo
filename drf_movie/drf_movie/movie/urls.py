from django.urls import path
from movie import views

#设置应用程序名称
app_name = 'movie'

#定义url模式列表
urlpatterns = [
    #根据路径视图Movielist进行映射，并命名为'list';
    path('',views.movie_list,name='list'),
    path('<int:pk>',views.MovieDetail.as_view(),name='detail'),
]