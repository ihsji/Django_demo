from django.contrib import admin
from app01.models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    #配置列表显示
    list_display = ('id', 'title')
    #配置过滤字段
    list_filter = ('id', 'title')
    #p配置搜索属性
    search_fields = ('id', 'title')

admin.site.register(Article,ArticleAdmin)