from django.contrib import admin
from team.models import Team
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    #显示字段
    list_display = ['id','name','title']
    #显示搜索栏
    search_fileds = ['name','title']

admin.site.register(Team,TeamAdmin)