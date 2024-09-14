from django.urls import path,re_path
# from app01.views import helloworld,article_create,article_detail,phone_detail
from . import views
urlpatterns = [
    path("create/",views.article_create,name="article_create"),
    path("<int:article_id>/<str:title>",views.article_detail,name="article_detail"),
    re_path("(?P<phone_number>1[3456789]\d{9})/$",views.phone_detail,name="phone_detail"),
    path('list/',views.list,name="artcle_list")
]