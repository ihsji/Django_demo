from django.contrib import admin
from account.models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    #配置列表显示
    list_display = ('username', 'email')
    #配置过滤字段
    list_filter = ('username','email')
    #p配置搜索属性
    search_fields = ('username','email')

admin.site.register(User,UserAdmin)
