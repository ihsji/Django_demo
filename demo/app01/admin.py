from django.contrib import admin
from app01.models import Article
# Register your models here.

def get_author(obj):
    return obj.user.username
class ArticleAdmin(admin.ModelAdmin):
    #配置列表显示
    list_display = ('id', get_author, 'title' ,'content')
    #配置过滤字段
    list_filter = ('id', 'title')
    #p配置搜索属性
    search_fields = ('id', 'title')
    #可以修改
    # list_editable = ('title','connect')

get_author.short_description= '作者名称'

admin.site.register(Article,ArticleAdmin)